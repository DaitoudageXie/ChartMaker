#coding=utf-8
import json
import matplotlib.pyplot as plt


class ChartMaker(object):
    def __init__(self):
        pass

    def make_gfx_chart(self, json_file):
        with open(json_file, 'r') as f:
            c_data = json.load(f)
            self.make_chart(c_data)

    def make_chart(self, data):
        print data
        x = []
        y = []
        for key in data.keys():
            for record in data[key]:
                if record[0] not in x:
                    x.append(record[0])
                if record[1] not in y:
                    y.append(record[1]-record[0])
        print x
        print y
        xlimit = (x.index(min(x)), x.index(max(x)))
        ylimit = (y.index(min(y)), y.index(max(y)))
        print xlimit
        print ylimit
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # plt.xlim()
        # plt.ylim()
        for key in data.keys():
            x1 = []
            y1 = []
            for record in data[key]:
                x1.append(record[0])
                y1.append(record[1]-record[0])
            plt.plot(x1, y1, label=key)
        plt.xlabel('intent vsync')
        plt.ylabel('draw time')
        plt.title('gfxinfo draw time')
        plt.legend()
        plt.show()
        #
        # plt.plot(cc, cc, label='linear')
        # plt.plot(cc, cc ** 2, label='double')
        # plt.plot(cc, cc ** 3, label='three')
        # plt.xlabel('x label')
        # plt.ylabel('y label')
        # plt.title("graph")
        # plt.legend()
        # plt.show()


if __name__ == '__main__':
    j_file = r'E:\workspace\ChartMaker\res\test.json'
    chart_maker = ChartMaker()
    chart_maker.make_gfx_chart(j_file)
