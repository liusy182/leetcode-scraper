
import json
import requests
import subprocess
import os
import re
import glob
import shutil

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
result_dir = 'output'
img_regex = re.compile(
    r'<img.+src=[\'\"]([^\'\"]+)[\'\"]', flags=re.IGNORECASE)


def get_all_questions():
    res = requests.post('https://leetcode.com/graphql',
        headers={
            'origin': 'https://leetcode.com',
            'user-agent': user_agent,
            'content-type': 'application/json',
        },
        data='{"operationName":"fetchQuestions","variables":{},"query":"query fetchQuestions {\\n  allQuestions {\\n    questionFrontendId\\n    title\\n    titleSlug\\n    __typename\\n  }\\n}\\n"}'
    )
    return res.json()['data']['allQuestions']


def download_questions(all_questions):
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    data_format = '{"operationName": "questionData", "variables": {"titleSlug": "%s"}, "query": "query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    envInfo\\n    libraryUrl\\n    __typename\\n  }\\n}\\n"}'
    for question in all_questions:
        print('\n' + question['questionFrontendId'] + ' ' + question['title'])
        question_dir = os.path.join(
            result_dir, question['questionFrontendId'] + '.' + question['title']).replace(' ', '')

        # skip if visited before
        if os.path.exists(question_dir):
            print('^^skipped')
            continue

        res = requests.post('https://leetcode.com/graphql',
            headers={
                'origin': 'https://leetcode.com',
                'user-agent': user_agent,
                'content-type': 'application/json',
            },
            data=data_format % question['titleSlug']
        )
        if res.status_code != 200:
            print(res.status_code)
            continue

        print(res.json())
        res_json = res.json()['data']['question']
       

        # because of premium subscription
        if not res_json['content']:
            print('^^premium subscription needed')
            continue

        os.makedirs(question_dir)
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
        with open(os.path.join(question_dir, 'meta.json'), 'w') as f:   
            json.dump(meta, f, indent=2)

        content = res_json['content']
        content = download_images(content, meta)
        with open(os.path.join(question_dir, 'question.md'), 'w') as f:
            f.write(content)


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
            sub[img] = './img/%s' % imgname
        counter += 1
    
    for k, v in sub.items():
        content = content.replace(k, v)
        
    return content

    

# for file in glob.glob(result_dir + '/**/*.md'):
#     dirname = os.path.dirname(file)
#     shutil.move(dirname, dirname.replace(' ', ''))
#     print(dirname)

def translate_to_mobile():
    allcontent = []
    for file in glob.glob(result_dir + '/**/question.md'):
        dirname = os.path.dirname(file)
        with open(os.path.join(dirname, 'meta.json'), 'r') as f:
            m = json.load(f)
            with open(file, 'r') as g:
                m['content'] = g.read()

            allcontent.append(m)
    
    with open(os.path.join(result_dir, 'all.json'), 'w') as f:
        json.dump(allcontent, f, indent=2)



all_questions = get_all_questions()
download_questions(all_questions)
# translate_to_mobile()
