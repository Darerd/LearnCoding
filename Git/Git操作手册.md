#### Git添加远程库的方法

以下是两个参考教程：

1. [添加远程库](https://www.liaoxuefeng.com/wiki/896043488029600/898732864121440)
2. [Git 远程仓库(Github)](https://www.runoob.com/git/git-remote-repo.html)

####  Git操作指令

```
#### 创建新文件夹 #############
mkdir demo				# 创建测试目录
cd demo/				# 进入测试目录

ls 						# 查看目录下的文件
git init 				# 初始化

#### 同步本地变化到远程仓库的方法 ##############
git add .				# 添加本地目录内所有文件
git commit -m "备注信息"	# 提交本地目录的修改内容
git push 				# 提交文件到远程仓库(Github)

#### 把github上的文件下载到本地 ###############
git pull 				# 从远程仓库下载数据到本地

### 同步github修改到本地的方法 ################
git fetch				# 从远程仓库下载新分支与数据
git merge				# 将远程仓库的修改同步到本地文件夹

### 查看、添加、编写文件  ############
cat readme.md			# 查看readme.md文件
touch test.txt			# 添加文件
vim test.txt			# 编写test.txt文件

#####  查看、添加、删除仓库  ##########
git remote				# 查看当前配置有哪些远程仓库
git remote -v 			# 查看当前远程仓库每个别名的实际链接地址
git remote add origin2  git@github.com:/Darerd/LearnCoding.git		# 添加仓库origin2
git remot rm origin2 	# 删除仓库origin2
```



