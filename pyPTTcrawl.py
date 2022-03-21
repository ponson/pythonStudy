from PyPtt import PTT
import sys


def handler(msg):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(msg + '\n')


# TODO create PTT object
ptt_bot = PTT.API(log_handler=handler)


# TODO login
try:
    ptt_bot.login("ponson", "jfNVir45")
except PTT.exceptions.LoginError:
    ptt_bot.log('登入失敗')
    sys.exit()
except PTT.exceptions.WrongIDorPassword:
    ptt_bot.log('帳號密碼錯誤')
    sys.exit()
except PTT.exceptions.LoginTooOften:
    ptt_bot.log('請稍等一下再登入')
    sys.exit()
ptt_bot.log('登入成功')

if ptt_bot.unregistered_user:
    print('未註冊使用者')

    if ptt_bot.process_picks != 0:
        print(f'註冊單處理順位 {ptt_bot.process_picks}')

if ptt_bot.registered_user:
    print('已註冊使用者')

# TODO Search keywords to find the post number
test_board_list = [
    'KoreaDrama',
    'marvel',
    'MLB',
    'Tech_Job',
    'movie',
]

for test_board in test_board_list:
    index = ptt_bot.get_newest_index(
        PTT.data_type.index_type.BBS,
        board=test_board
    )
    print(f'{test_board} 最新文章編號 {index}')
'''
test_list = [
    ('KoreaDrama', PTT.data_type.post_search_type.KEYWORD, 'Arin')
]
for (test_board, search_type, condition) in test_list:
    index = ptt_bot.get_newest_index(
        PTT.data_type.index_type.BBS,
        test_board,
        search_type=search_type,
        search_condition=condition,
    )
    print(f'{test_board} 最新文章編號 {index}')

    post = ptt_bot.get_post(
        test_board,
        post_index=index,
        search_type=search_type,
        search_condition=condition,
    )

    print('標題:')
    print(post.title)
    print('內文:')
    print(post.content)
    print('=' * 50)
'''
# call ptt_bot other api
# TODO get post content
'''
post_info = ptt_bot.get_post(
    'Road_Running',
    post_index=35814)


# TODO 資料整理，改成Data Frame存放，轉成CSV檔，方便查看
# TODO 將資料標題、單行內容、連結丟到LINE chat bot上面通知使用者

if post_info is None:
    print('post_info is None')
    sys.exit()

if post_info.delete_status != PTT.data_type.post_delete_status.NOT_DELETED:
    if post_info.delete_status == PTT.data_type.post_delete_status.MODERATOR:
        print(f'[板主刪除][{post_info.author}]')
    elif post_info.delete_status == PTT.data_type.post_delete_status.AUTHOR:
        print(f'[作者刪除][{post_info.author}]')
    elif post_info.delete_status == PTT.data_type.post_delete_status.UNKNOWN:
        print(f'[不明刪除]')
    sys.exit()

if post_info.is_lock:
    print('[鎖文]')
    sys.exit()

if not post_info.pass_format_check:
    print('[不合格式]')
    sys.exit()

print('Board: ' + post_info.board)
print('AID: ' + post_info.aid)
print('index:' + str(post_info.index))
print('Author: ' + post_info.author)
print('Date: ' + post_info.date)
print('Title: ' + post_info.title)
print('content: ' + post_info.content)
print('Money: ' + str(post_info.money))
print('URL: ' + post_info.web_url)
print('IP: ' + post_info.ip)
# 在文章列表上的日期
print('List Date: ' + post_info.list_date)
print('地區: ' + post_info.location)
# Since 0.8.19
# 有可能為 None，因為不是每篇文在文章列表都有推文數
print('文章推文數: ' + post_info.push_number)

if post_info.is_unconfirmed:
    # Since 0.8.30
    print('待證實文章')

push_count = 0
boo_count = 0
arrow_count = 0

for push_info in post_info.push_list:
    if push_info.type == PTT.data_type.push_type.PUSH:
        push_type = '推'
        push_count += 1
    if push_info.type == PTT.data_type.push_type.BOO:
        push_type = '噓'
        boo_count += 1
    if push_info.type == PTT.data_type.push_type.ARROW:
        push_type = '箭頭'
        arrow_count += 1

    author = push_info.author
    content = push_info.content

    buffer = f'{author} 給了一個{push_type} 說 {content}'
    if push_info.ip is not None:
        buffer += f'來自 {push_info.ip}'
    buffer += f'時間是 {push_info.time}'
    print(buffer)

print(f'Total {push_count} Pushs {boo_count} Boo {arrow_count} Arrow')
'''
ptt_bot.logout()