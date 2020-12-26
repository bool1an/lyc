n = int(input())
st = set()
count = 0
st_c = set()
for i in range(n):
    k = input()
    if k in st:
        count += 1
        st_c.add(k)
    st.add(k)
print(count + len(st_c))