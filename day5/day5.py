items = list(open('day5.txt'))
tt = str.maketrans({'B':'1','F':'0','R':'1','L':'0'})
decode = lambda seat: int(seat.translate(tt), 2)
seats = set(map(decode, items))
print(max(seats))
all_ = set(range(min(seats), max(seats)))
print(all_ - seats)
