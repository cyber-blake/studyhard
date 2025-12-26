#
# * n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.
def flavius(n, k):

    def josef(list_of_people, k):
        list_of_people = [i for i in range(1, n + 1)]
        if len(list_of_people) == 1:
            return list_of_people[0]
        elif len(list_of_people) > 1:
            list_of_people.pop(list_of_people[len(list_of_people) % k])
            print(list_of_people)
            return josef(list_of_people, k - 1)


n = int(input())
k = int(input())
flavius(n, k)
