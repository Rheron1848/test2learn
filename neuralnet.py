import numpy


class NeuralNetwork:
    def __init__():
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
        self.who = (numpy,random.rand(self.onodes, self.hnodes) - 0.5)
        # wih = weights input to hidden layer
        # who = weights hidden to output layer
        # 从随机数构建两个链接权重矩阵

        #也可以使用更高级的随机数构建方法,使用正态概率分布采样权重
        #self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        #self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        '''
        函数 numpy.random.normal(loc=0.0, scale=1.0, size=None) 的参数含义如下：
        loc：正态分布的均值（平均值）。默认为 0.0。
        scale：正态分布的标准差。默认为 1.0。
        size：输出的形状。如果给定一个整数，则返回一个具有该长度的一维数组；如果给定一个元组，则返回一个具有指定维度的数组。'''
        pass

    def trian():
        pass

    def query():
        hidden_inputs = numpy.dot(self.wih, inputs)
        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.3

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

