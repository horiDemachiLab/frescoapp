


##時速による加点
def additional_point_by_each_speed(speed):
    if speed <= 50:
        return speed
    elif speed >50 and speed <=60:
        return speed * 1.1
    elif speed >60 and speed <=70:
        return speed * 1.3
    elif speed >70 and speed <=80:
        return speed * 1.5
    elif speed >80 and speed <=90:
        return speed * 1.7
    elif speed > 90:
        return speed * 1.9


##落球による減点
def substracting_point_by_drop(drop_num):
    if drop_num <=5:
        return 0
    elif drop_num = 6:
        return -100
    elif drop_num = 7:
        return -200
    elif drop_num = 8:
        return -300
    elif drop_num = 9:
        return -400
    elif drop_num = 10:
        return -500
    elif drop_num = 11:
        return -600
    elif drop_num = 12:
        return -700
    elif drop_num = 13:
        return -800
    elif drop_num = 14:
        return -900
    elif drop_num >= 15 and drop_num < 30:
        return -1000
    elif drop_num > 30:
        #-1000点にして、ゲームセット試合終了にする
        return -1000:



##平均時速による加点
#２選手の平均時速による加点
def additional_point_by_both_player_average_speed(speed):
    return 0

#playerAの平均時速による加点
def additional_point_by_a_player_average_speed(speed):
    if speed <= 50:
        return 1000
    elif speed >50 and speed <=60:
        return 2000
    elif speed >60 and speed <=70:
        return 3000
    elif speed >70 and speed <=80:
        return 4000
    elif speed >80 and speed <=90:
        return 5000
    elif speed > 90:
        return 6000

#playerBの平均時速による加点
def additional_point_by_b_player_average_speed(speed):
    if speed <= 50:
        return 1000
    elif speed >50 and speed <=60:
        return 2000
    elif speed >60 and speed <=70:
        return 3000
    elif speed >70 and speed <=80:
        return 4000
    elif speed >80 and speed <=90:
        return 5000
    elif speed > 90:
        return 6000


##最大時速による加点
#２選手の最大時速による加点
def additional_point_by_both_player_max_speed(speed):
    return 0

#playerAの最大時速による加点
def additional_point_by_a_player_max_speed(speed):
    if speed <=70:
        return 0
    elif speed >70 and speed <=80:
        return 4000
    elif speed >80 and speed <=90:
        return 5000
    elif speed > 90:
        return 6000

#playerBの最大時速による加点
def additional_point_by_b_player_max_speed(speed):
    if speed <=70:
        return 0
    elif speed >70 and speed <=80:
        return 4000
    elif speed >80 and speed <=90:
        return 5000
    elif speed > 90:
        return 6000

##アタック数による加点
#２選手のアタック数による加点
def additional_point_by_both_player_attack_num(num):
    return 0

#playerAのアタック数による加点
def additional_point_by_a_player_attack_num(num):
    if num <= 150:
        return 0
    elif num >150 and num <= 200:
        return 1000
    elif num >150 and num <= 200:
        return 2000
    elif num >200 and num <= 250:
        return 3000
    elif num >250 and num <= 300:
        return 4000
    elif num > 300:
        return 5000

#playerBのアタック数による加点
def additional_point_by_a_player_attack_num(num):
    if num <= 150:
        return 0
    elif num >150 and num <= 200:
        return 1000
    elif num >150 and num <= 200:
        return 2000
    elif num >200 and num <= 250:
        return 3000
    elif num >250 and num <= 300:
        return 4000
    elif num > 300:
        return 5000
