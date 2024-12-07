# repoGitsubmodule

git submodule调试

# 添加repoExample项目为子模块

git submodule add -b main https://github.com/firstelfin/repoExample.git repo/repoExample

此命令会生成文件 `.gitmodules`

```shell
[submodule "repo/repoExample"]
	path = repo/repoExample
	url = https://github.com/firstelfin/repoExample.git
	branch = main
```

# 初始化子模块

git submodule update --init --recursive


# 删除子模块

1. git submodule  deinit --force repo/repoExample  清除文件夹 'repo/repoExample'
2. 删除.gitmodules记录: git rm -f repo/repoExample
3. 删除缓存：git rm --cache repo/repoExample
4. 删除文件夹：rm -rf .git/modules/repo/repoExample
5. 删除文件夹：rm -rf repo/repoExample
6. 删除.gitmodules记录: git rm -f repo/repoExample

---

```shell
git submodule  deinit --force repo/repoExample
git rm -f --cache repo/repoExample
rm -rf repo/repoExample
rm -rf .git/modules/repo/repoExample

```


参考资源

1. git官网文档：https://git-scm.com/docs
