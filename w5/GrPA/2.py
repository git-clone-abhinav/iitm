def user_score(read_count, reply_count, new_post_count):
    score = (read_count*1) + (reply_count*3) + (reply_count*5)
    return "Leader" if score > 50 else "Basic"