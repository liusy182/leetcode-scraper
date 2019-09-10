
import json
import requests
import subprocess
import os
import re
import glob
import uuid

result_dir = 'output'
img_regex = re.compile(
    r'<img.+src=[\'\"]([^\'\"]+)[\'\"]', flags=re.IGNORECASE)

def download_questions():
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    all_questions = []
    with open('all_questions.json', 'r') as f:
        all_questions = json.load(f)

    data_format = '{"operationName": "questionData", "variables": {"titleSlug": "%s"}, "query": "query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    envInfo\\n    libraryUrl\\n    __typename\\n  }\\n}\\n"}'
    for question in all_questions:
        res = requests.post('https://leetcode.com/graphql',
            headers={
                'origin': 'https://leetcode.com',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'content-type': 'application/json',
            },
            data=data_format % question['titleSlug']
            # data='{"operationName": "questionData", "variables": {"titleSlug": "set-intersection-size-at-least-two"}, "query": "query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    contributors {\\n      username\\n      profileUrl\\n      avatarUrl\\n      __typename\\n    }\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    envInfo\\n    libraryUrl\\n    __typename\\n  }\\n}\\n"}'
        )

        res_json = res.json()['data']['question']

        # print('===========================================')
        # print(question)
        # print('-------------------------------')
        # print(res_json)

        # because of premium subscription
        if not res_json['content']:
            continue

        question_dir = os.path.join(result_dir, question['questionFrontendId'] + '. ' + question['title'])
        if not os.path.exists(question_dir):
            os.makedirs(question_dir)

        with open(os.path.join(question_dir, 'question.md'), 'w') as f:
            f.write(res_json['content'])

        with open(os.path.join(question_dir, 'meta.json'), 'w') as f:
            json.dump({
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
            }, f, indent=2)


def download_images():    
    for file in glob.glob(result_dir + '/**/*.md'):
        filecontent, imgs = None, []
        with open(file, 'r') as f:
            filecontent = f.read()
            imgs = img_regex.findall(filecontent)
            if len(imgs) == 0 or imgs[0].startswith('./img'):
                continue
        
        dirname = os.path.dirname(file)
        imgprefix = os.path.basename(file)
        with open(os.path.join(dirname, 'meta.json'), 'r') as f:
            imgprefix = json.load(f)['slug']
        
        imgdir = os.path.join(dirname, 'img')
        if not os.path.exists(imgdir):
            os.makedirs(imgdir)

        sub = {}
        counter = 1
        for img in imgs:
            if img in sub:
                continue

            _, ext = os.path.splitext(img)
            res = requests.get(img)
            imgname = imgprefix + '_' + str(counter) + ext
            with open(os.path.join(imgdir, imgname), 'wb') as f:
                f.write(res.content)
                sub[img] = './img/%s' % imgname
            counter += 1
        
        for k, v in sub.items():
            filecontent = filecontent.replace(k, v)

        with open(file, 'w') as f:
            f.write(filecontent)
        print(file)
        break

download_images()
