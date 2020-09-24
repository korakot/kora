import os

os.system("curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg")
os.system("mv bazel.gpg /etc/apt/trusted.gpg.d/")
with open('/etc/apt/sources.list.d/bazel.list', 'w') as f:
    f.write("deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8")
os.system("apt update && apt install bazel")
