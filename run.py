
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from lcscraper.spiders.solution import SolutionSpider
from multiprocessing import Process, Queue
import json
import requests
import subprocess
import os
import re
import glob
import shutil

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

result_dir = 'output'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

img_regex = re.compile(
    r'<img.+src=[\'\"]([^\'\"]+)[\'\"]', flags=re.IGNORECASE)


def get_all_questions():
    res = requests.post('https://leetcode.com/graphql',
        headers={
            'origin': 'https://leetcode.com',
            'user-agent': user_agent,
            'content-type': 'application/json',
        },
        data='{"operationName":"fetchQuestions","variables":{},"query":"query fetchQuestions {\\n  allQuestions {\\n    questionFrontendId\\n    title\\n    titleSlug\\n    }\\n}\\n"}'
    )
    questions = res.json()['data']['allQuestions']
    with open(os.path.join(result_dir, 'all_questions.json'), 'w') as f:
            json.dump(questions, f, indent=2)
    return questions


def download_all(all_questions):
    data_format = '{"operationName": "questionData", "variables": {"titleSlug": "%s"}, "query": "query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    envInfo\\n    libraryUrl\\n    __typename\\n  }\\n}\\n"}'
    for question in all_questions[:10]:
        print('\n' + question['questionFrontendId'] + ' ' + question['title'])
        question_dir = os.path.join(
            result_dir, question['questionFrontendId'] + '.' + question['title']).replace(' ', '')
        if not os.path.exists(question_dir):
            os.makedirs(question_dir)

        meta = download_question(question, question_dir)
        download_solution(meta, question_dir)
        

def download_images(content, meta):
    imgs = img_regex.findall(content)
    if len(imgs) == 0:
        return content
    
    imgdir = os.path.join(result_dir, 'img')
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)
   
    sub = {}
    counter = 1
    for img in imgs:
        if img in sub:
            continue
        _, ext = os.path.splitext(img)
        res = requests.get('https://leetcode.com' + img if img.startswith('/') else img)
        imgname = meta['slug'] + '_' + str(counter) + ext
        with open(os.path.join(imgdir, imgname), 'wb') as f:
            f.write(res.content)
            sub[img] = '../img/%s' % imgname
        counter += 1
    
    for k, v in sub.items():
        content = content.replace(k, v)
        
    return content


def download_question(question, question_dir):
    question_fname = os.path.join(question_dir, 'question.md')
    meta_fname = os.path.join(question_dir, 'meta.json')
    if os.path.exists(meta_fname) and os.path.exists(question_fname):
        print('^^ skip downloaded question')
        with open(meta_fname, 'r') as f:
            return json.load(f)

    data_format = '{"operationName": "questionData", "variables": {"titleSlug": "%s"}, "query": "query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    envInfo\\n    libraryUrl\\n    __typename\\n  }\\n}\\n"}'
    res = requests.post('https://leetcode.com/graphql',
        headers={
            'origin': 'https://leetcode.com',
            'user-agent': user_agent,
            'content-type': 'application/json',
        },
        data=data_format % question['titleSlug']
    )
    if res.status_code != 200:
        print('^^ error status code ' + res.status_code)
        return None

    print(res.json())
    res_json = res.json()['data']['question']

    meta = {
        'id': question['questionFrontendId'],
        'title': question['title'],
        'slug': question['titleSlug'],
        'difficulty': res_json['difficulty'],
        'likes': res_json['likes'],
        'dislikes': res_json['dislikes'],
        'dislikes': res_json['dislikes'],
        'hints': res_json['hints'],
        'isPaidOnly': res_json['isPaidOnly'],
        'similarQuestions': res_json['similarQuestions'],
        'solution': res_json['solution'],
        'topicTags': list(map(lambda tag: tag['name'], res_json['topicTags'])),
    }
    with open(meta_fname, 'w') as f:
        json.dump(meta, f, indent=2)

    if not res_json['content']:
        print('^^empty content')
    else:
        content = download_images(res_json['content'], meta)
        with open(question_fname, 'w') as f:
            f.write(content)

    return meta


def run_spider(spider, *args, **kwargs):
    def f(q):
        try:
            runner = CrawlerRunner()
            deferred = runner.crawl(spider, *args, **kwargs)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result

def download_solution(meta, question_dir):
    pass
    # if meta and meta['solution'] and meta['solution']['canSeeDetail']:
    #     run_spider(SolutionSpider, meta=meta, question_dir=question_dir)


def translate_to_mobile():
    allcontent = []
    for file in glob.glob(result_dir + '/**/question.md'):
        dirname = os.path.dirname(file)
        with open(os.path.join(dirname, 'meta.json'), 'r') as f:
            m = json.load(f)
            with open(file, 'r') as g:
                m['content'] = g.read()
            if os.path.exists(os.path.join(dirname, 'solution.md')):
                with open(os.path.join(dirname, 'solution.md'), 'r') as g:
                    m['solution']['content'] = g.read()
                    del m['solution']['__typename']

            allcontent.append(m)
    
    with open(os.path.join(result_dir, 'all.json'), 'w') as f:
        json.dump(allcontent, f, indent=2)



all_questions = get_all_questions()
download_all(all_questions)
# translate_to_mobile()
