'''
1 选择人物
2 购买武器 金币
3 打仗 赢得金币
4 选择删除武器
5 查看武器
6 退出游戏
'''
import random

def main():
    print('*'*40)
    print(f'{"欢迎来到王者荣耀":^32}')
    print('*'*40)
    roles = ['鲁班', '后羿', '李白', '孙尚香', '貂蝉', '诸葛亮']
    role = roles[int(input('请选择人物：(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮)\n'))-1]
    coins = 1000
    # 武器库
    weapons = [['屠龙刀',500],['火尖枪',600],['碧血剑',700],['天龙戟',1000]]
    # 用户的武器列表
    weapon_list = []

    print(f'欢迎 {role} ！\n当前金币是：{coins}')
    while True:
        choice = input('请选择：\n 1.购买武器\n 2.打仗\n 3.卖出武器\n 4.查看武器\n 5.退出\n')
        
        if choice == '1':
            # 购买武器
            print('  欢迎进入武器库！\n')
            for i,v in enumerate(weapons):
                print(i+1,v[0],v[1],sep='       ')
            while True:
                # 提示 购买武器
                w = int(input('  请选择要购买的武器序号：\n'))
                #如果输入非法，则退出循环
                if w not in [1,2,3,4]:
                    print('  输入的错误，请重新选择')
                    continue
                elif weapons[w-1][0] in weapon_list:
                    print('  不能购买已装备的武器！请重新选择')
                else:
                    break
            # 购买武器
            if coins >= weapons[w-1][1]:
                coins -= weapons[w-1][1]
                weapon_list.append(weapons[w-1][0])
                print(f'  已购买 {weapons[w-1][0]}')
                print('  已装备武器：',weapon_list)
            else:
                print('  金币数不足，请选择其他武器 或者 去挣金币！')

        elif choice == '2':
            # 打怪，赢取金币
            print('  进入战场')
            if weapon_list:
                #如果有武器
                #选择武器
                print('  请选择以下已装备武器：\n')
                for i,v in enumerate(weapon_list):
                    print(i+1, v)
                w = int(input('  输入武器序号：\n'))
                weapon = weapons[w-1]
                
                #进入战争状态  默认跟张飞对战
                enemy = {'name':'张飞','power':80} # 假设用此种格式定义敌人属性
                while True:
                    rand1 = random.randint(1,20)
                    rand2 = random.randint(1,20)
                    if rand1 > rand2:
                        print('  此局你获胜！')
                        # 获胜奖励100个金币，  此处可以根据对手不同，奖励不同
                        coins += 100
                        print('  目前金币数：',coins)
                    elif rand1 < rand2:
                        print(f'  此局{enemy["name"]}获胜！')
                        # coins -= 50
                    else:
                        print('  平局，请继续')
                    if input('  是否继续对战？(y/n)')!='y':
                        break
            else:
                print('  还没有武器,请购买武器!')

        elif choice == '3':
            # 卖出 武器
            while True:
                if weapon_list:
                    for i,v in enumerate(weapon_list):
                        print(i+1, v)
                    w = int(input('  请输入要卖出的武器序号：\n'))
                    wname = weapon_list[w-1]
                    print('  已经卖出武器：',wname)
                    for i in weapons: # 从weapons列表中找到武器对应的价格，再增加到coins中
                        if wname in i:
                            coins += i[1]
                            print('  换得金币：', i[1])
                            print('  现有金币：', coins)
                            break

                    del(weapon_list[w-1])
                    if input('  继续卖出武器？(y/n)') == 'y':
                        continue
                    else:
                        break
                else:
                    print('  没有武器,请购买武器!')
                    break
                    
        elif choice == '4':
            # 查看武器
            print('  拥有以下武器：\n')
            for i,v in enumerate(weapon_list):
                print(i+1, v)
        elif choice == '5':
            # 退出游戏
            if input('  确定要离开游戏吗？(y/n)')=='y':
                print('Game Over')
                break
            else:
                continue
            
if __name__ == "__main__":
    main()