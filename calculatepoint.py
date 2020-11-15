


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



#平均時速、最大時速、アタック数による加点に関する以下の6メソッドは未確定のため現状仮置き。
def additional_point_by_both_player_average_speed(speed):
    if speed <= 70:
        return 0
    elif speed >70:
        return 1000 

def additional_point_by_each_player_average_speed(speed):
    if speed <= 70:
        return 0
    elif speed >70:
        return 1000

def additional_point_by_both_player_max_speed(speed):
    if speed <= 90:
        return 0
    elif speed >90:
        return 1000 

def additional_point_by_each_player_max_speed(speed):
    if speed <= 90:
        return 0
    elif speed >90:
        return 1000

def additional_point_by_both_player_attack_num(num):
    if num <= 100:
        return 0
    elif num >100:
        return 1000

def additional_point_by_each_player_attack_num(num):
    if num <= 100:
        return 0
    elif num >100:
        return 1000



print(speed_additional_point(60))


