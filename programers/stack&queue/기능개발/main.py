import math

def solution(progresses, speeds):
    def remain_day(progress,speed):
        return math.ceil((100-progress)/speed)
    remain_days = list(map(remain_day,progresses,speeds))
    release = remain_days[0]
    answer = []
    count=0
    for idx,remain_day in enumerate(remain_days):
        if release>=remain_day:
            count +=1
        else:
            release=remain_day
            answer.append(count)
            count=1
        if idx==len(remain_days)-1:
            answer.append(count)
    return answer