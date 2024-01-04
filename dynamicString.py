word="abcfignringiozqlfnznqrstuvwxinad"
pointer=0
current_sum=1
maximum_sum=0
i=1
while i<len(word):
    while i<len(word) and  word[i]>word[i-1] :
        current_sum+=1
        i+=1
    else:
        maximum_sum=max(maximum_sum,current_sum)
        current_sum=1
    i+=1

print(maximum_sum)
