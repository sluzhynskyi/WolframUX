import wolframalpha  as wf

client = wf.Client("JYETQ2-WP5J5GX3ER")  # app_ID is the app id

q = "Solve 274770*x**1.2 + 8271.8*x**2.2 + 79.555*x**3.2 + 0.22184*x**4.2 - 35435557377 = 0"
res = client.query(q)
answer = next(res.results).text
print(answer)