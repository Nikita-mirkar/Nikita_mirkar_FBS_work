# amount = int(input("Enter the amount: "))
# original_amount = amount
# total_notes = 0
# note = 500
# print("notd for amount: ", print)
# for i in range(6):
#     if amount >= note:
#         count = amount // note
#         total_notes += count
#         print("note of ",note , count)
#         amount %= note
#     if note == 500:
#         note = 200
#     elif note == 200:
#         note = 100
#     elif note == 100:
#         note = 50
#     elif note == 50:
#         note = 20
#     elif note == 20:
#         note = 10

# print("total notes are used: ", total_notes)

amount= int(input("Enter the amount: "))
notes= (500,200,100,50,20,10)

for i in notes:
    if(amount >= i):
        count= amount//i
        amount= amount %i
        print(f"{i} x {count}")