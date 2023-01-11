tempstr = "Python, C++, Kotlin, Java, HTML, CSS, Javascript, SQL, Node.js"

out = (" " + tempstr).split(",")
sortout = sorted(out)
print(*sortout, sep=',')
