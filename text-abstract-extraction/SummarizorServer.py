from flask import Flask, request, render_template
import json

from Summarizor import Summarizor


app = Flask(__name__)
#CORS(app, supports_credentials=True)

@app.route('/start', methods=['GET'])
def start():
    return json.dumps({'message是 是是': 'start_success 操'})


@app.route('/kill', methods=['POST'])
def kill():
    return json.dumps({'message': 'kill_success'})


@app.route('/get_summary', methods=['GET', 'POST'])
def get_summary():
    title = request.args.get('tt')
    content = request.args.get('ctt')
    proportion = request.args.get('ppt')
    print("收到消息：", 'tt', title, 'ppt', proportion, 'ctt', content)
    if title != None and content != None and proportion != None:
        summarySentences = summarizor.summarize(content, title, proportion=float(proportion))
        res = "".join(summarySentences)
        print('生成摘要：', res, "\n---------------------------------------------------")
    else:
        res = "您未正确按要求输入数据！"

    return render_template("index.html", res = res)

if __name__ == '__main__':
    summarizor = Summarizor()

    app.run(port=9998)

    # 浏览器地址栏中输入进行测试：
	# http://127.0.0.1:9999/get_summary?tt={}&ctt={}&ppt={}
    # http://127.0.0.1:9999/get_summary?tt=fjfejsfjes&ctt=2222222222222222333333333eeeeeeee%E3%80%82%E4%B8%96%E7%95%8C%E7%BA%A7%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%90%84%E4%B8%AA%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%A4%A9%E4%BD%BF%E3%80%82%E5%90%84%E4%B8%AA%E5%A4%A9%E4%BD%BF%E3%80%82&ppt=0.3
    # http://127.0.0.1:9999/get_summary?tt=%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E8%B0%88%E8%B5%B7%E8%AF%89%E4%BA%AC%E4%B8%9C%EF%BC%9A%E6%9C%AA%E7%BB%8F%E8%AE%B8%E5%8F%AF%E5%B0%86%E7%A5%9E%E8%88%9F%E4%BA%A7%E5%93%81%E9%99%8D%E4%BB%B7%E9%94%80%E5%94%AE%E5%90%8E%E8%A6%81%E8%BF%94%E5%88%A9&ctt=%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E6%8A%AB%E9%9C%B2%E4%BA%86%E8%B5%B7%E8%AF%89%E4%BA%AC%E4%B8%9C%E8%83%8C%E5%90%8E%E5%8F%8C%E6%96%B9%E7%9A%84%E7%BA%A0%E8%91%9B%E3%80%822%E6%9C%8820%E6%97%A5%EF%BC%8C%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E5%85%AC%E5%BC%80%E6%8C%87%E8%B4%A3%E4%BA%AC%E4%B8%9C%E6%8B%96%E6%AC%A0%E7%A5%9E%E8%88%9F%E8%B6%853%E4%BA%BF%E8%B4%A7%E6%AC%BE%EF%BC%8C%E5%B9%B6%E5%B7%B2%E4%BA%8E2%E6%9C%8818%E6%97%A5%E5%9C%A8%E5%8C%97%E4%BA%AC%E5%B8%82%E7%AC%AC%E4%BA%8C%E4%B8%AD%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2%E5%90%91%E4%BA%AC%E4%B8%9C%E6%8F%90%E8%B5%B7%E8%AF%89%E8%AE%BC%EF%BC%8C%E8%AF%89%E8%AE%BC%E6%A0%87%E7%9A%84%E9%A2%9D%E4%B8%BA%E4%BA%BA%E6%B0%91%E5%B8%813.383%E4%BA%BF%E5%85%83%E3%80%82%E5%BD%93%E5%A4%A9%EF%BC%8C%E4%BA%AC%E4%B8%9C%E6%96%B9%E9%9D%A2%E5%81%9A%E5%87%BA%E5%9B%9E%E5%BA%94%E7%A7%B0%EF%BC%8C%E5%9B%A0%E7%A5%9E%E8%88%9F%E8%BF%9D%E5%8F%8D%E5%8F%8C%E6%96%B9%E7%AD%BE%E7%BD%B2%E7%9A%84%E4%BA%A7%E5%93%81%E8%B4%AD%E9%94%80%E5%8D%8F%E8%AE%AE%E6%9D%A1%E6%AC%BE%EF%BC%8C%E5%AF%BC%E8%87%B4%E5%85%B6%E6%9C%AA%E7%BB%93%E7%AE%97%E8%B4%A7%E6%AC%BE%E8%A2%AB%E6%9A%82%E7%BC%93%E6%94%AF%E4%BB%98%E3%80%822%E6%9C%8821%E6%97%A5%EF%BC%8C%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E5%8F%91%E5%B8%83%E5%BE%AE%E5%8D%9A%E5%88%97%E5%87%BA%E4%BA%86%E4%B8%8E%E4%BA%AC%E4%B8%9C%E7%9A%84%E9%83%A8%E5%88%86%E5%BE%80%E6%9D%A5%E4%BF%A1%E5%87%BD%EF%BC%8C%E6%8A%AB%E9%9C%B2%E4%BA%86%E4%B8%8E%E4%BA%AC%E4%B8%9C%E4%B9%8B%E9%97%B4%E7%9A%84%E7%BA%A0%E7%BA%B7%E7%BB%86%E8%8A%82%EF%BC%8C%E4%BA%89%E8%AE%AE%E7%84%A6%E7%82%B9%E5%9B%B4%E7%BB%95%E5%9C%A82019%E5%B9%B4%E7%9A%84%E5%8F%8C11%E6%B4%BB%E5%8A%A8%E4%B8%8A%E3%80%82%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E7%A7%B0%EF%BC%9A%E4%BA%AC%E4%B8%9C%E5%8E%BB%E5%B9%B4%E5%8F%8C11%E9%80%BC%E8%BF%AB%E7%A5%9E%E8%88%9F%E4%BA%8C%E9%80%89%E4%B8%80%EF%BC%8C%E4%B8%8D%E5%87%86%E7%A5%9E%E8%88%9F%E5%8F%82%E5%8A%A0%E5%A4%A9%E7%8C%AB%E5%8F%8C11%E6%B4%BB%E5%8A%A8%EF%BC%8C%E8%A2%AB%E7%A5%9E%E8%88%9F%E6%8B%92%E7%BB%9D%E3%80%82%E9%9A%8F%E5%90%8E%E4%BA%AC%E4%B8%9C%E6%9C%AA%E7%BB%8F%E7%A5%9E%E8%88%9F%E8%AE%B8%E5%8F%AF%EF%BC%8C%E5%BC%BA%E8%A1%8C%E5%B0%86%E7%A5%9E%E8%88%9F%E4%BA%A7%E5%93%81%E9%99%8D%E4%BB%B7%E9%94%80%E5%94%AE%EF%BC%8C%E5%B9%B6%E5%A3%B0%E7%A7%B0%E4%BA%AC%E4%B8%9C%E5%8F%8C11%E6%9C%89%E7%99%BE%E4%BA%BF%E8%A1%A5%E8%B4%B4%EF%BC%8C%E6%97%A0%E9%9C%80%E7%A5%9E%E8%88%9F%E6%89%BF%E6%8B%85%E4%BB%BB%E4%BD%95%E8%B4%B9%E7%94%A8%E3%80%82%E8%87%B3%E7%BB%93%E7%AE%97%E6%97%B6%EF%BC%8C%E4%BA%AC%E4%B8%9C%E5%8D%B4%E8%A6%81%E6%B1%82%E7%A5%9E%E8%88%9F%E6%94%AF%E4%BB%981559%E4%B8%87%E5%85%83%E8%BF%94%E5%88%A9%EF%BC%8C%E7%A5%9E%E8%88%9F%E4%B8%8D%E5%90%8C%E6%84%8F%E6%AD%A4%E9%83%A8%E5%88%86%E8%BF%94%E5%88%A9%EF%BC%8C%E4%BA%AC%E4%B8%9C%E5%B0%B1%E6%89%A3%E4%B8%8B%E4%BA%86%E7%A5%9E%E8%88%9F%E5%85%A8%E9%83%A8%E8%B4%A7%E6%AC%BE%E3%80%82%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E8%BF%98%E8%A1%A8%E7%A4%BA%EF%BC%8C%E4%B8%BA%E4%BA%86%E9%80%BC%E8%BF%AB%E7%A5%9E%E8%88%9F%E5%90%8C%E6%84%8F%E6%94%AF%E4%BB%98%E6%AD%A4%E9%83%A8%E5%88%86%E9%99%8D%E4%BB%B7%E6%8D%9F%E5%A4%B1%EF%BC%8C%E4%BA%AC%E4%B8%9C%E5%AF%B9%E7%A5%9E%E8%88%9F%E9%87%87%E7%94%A8%E4%BA%86%E4%BA%94%E9%A1%B9%E6%8E%AA%E6%96%BD%EF%BC%9A%E4%BA%A7%E5%93%81%E6%90%9C%E7%B4%A2%E9%99%8D%E6%9D%83%E3%80%81%E4%B8%8D%E8%AE%A9%E5%8F%82%E5%8A%A0%E4%BB%BB%E4%BD%95%E6%B4%BB%E5%8A%A8%E3%80%81%E7%BC%BA%E8%B4%A7%E4%BA%A7%E5%93%81%E4%B8%8D%E4%BA%88%E8%AE%A2%E8%B4%A7%E3%80%81%E5%85%A8%E7%BA%BF%E4%BA%A7%E5%93%81%E4%B8%8B%E6%9E%B6%E3%80%81%E4%B8%8D%E4%BA%88%E7%BB%93%E7%AE%97%E8%B4%A7%E6%AC%BE%E3%80%82%E5%AF%B9%E4%BA%8E%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E7%9A%84%E6%8C%87%E6%8E%A7%EF%BC%8C%E4%BA%AC%E4%B8%9C%E6%96%B9%E9%9D%A2%E5%90%91%E6%BE%8E%E6%B9%83%E6%96%B0%E9%97%BB%E8%AE%B0%E8%80%85%E8%A1%A8%E7%A4%BA%EF%BC%8C%E5%AF%B9%E4%BA%8E%E5%8F%8C%E6%96%B9%E7%9A%84%E4%BA%89%E8%AE%AE%EF%BC%8C%E6%88%91%E4%BB%AC%E7%9B%B8%E4%BF%A1%E6%B3%95%E5%BE%8B%E4%BC%9A%E5%81%9A%E5%87%BA%E5%85%AC%E6%AD%A3%E7%9A%84%E8%A3%81%E5%86%B3%E3%80%82%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E5%AE%98%E7%BD%91%E6%98%BE%E7%A4%BA%EF%BC%8C%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E6%88%90%E7%AB%8B%E4%BA%8E2001%E5%B9%B4%EF%BC%8C%E6%98%AF%E4%B8%80%E5%AE%B6%E4%BB%A5IT%E3%80%81IA%E4%B8%BA%E4%B8%BB%E4%B8%9A%EF%BC%8C%E4%BB%A5%E7%94%B5%E8%84%91%E6%8A%80%E6%9C%AF%E5%BC%80%E5%8F%91%E4%B8%BA%E6%A0%B8%E5%BF%83%EF%BC%8C%E9%9B%86%E7%A0%94%E5%8F%91%E3%80%81%E7%94%9F%E4%BA%A7%E3%80%81%E9%94%80%E5%94%AE%E4%B8%BA%E4%B8%80%E4%BD%93%E7%9A%84%E5%9B%BD%E5%AE%B6%E7%BA%A7%E9%AB%98%E7%A7%91%E6%8A%80%E4%BC%81%E4%B8%9A%E3%80%82%E7%9B%AE%E5%89%8D%EF%BC%8C%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E5%9C%A8%E4%BA%AC%E4%B8%9C%E4%B8%8A%E6%9C%89%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E4%BA%AC%E4%B8%9C%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%EF%BC%8C%E5%90%8C%E6%97%B6%E4%B9%9F%E6%9C%89%E7%A5%9E%E8%88%9F%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5%E6%97%97%E8%88%B0%E5%BA%97%E3%80%82%E9%99%84%EF%BC%9A%E7%A5%9E%E8%88%9F%E7%94%B5%E8%84%91%E5%BE%AE%E5%8D%9A&ppt=0.3
