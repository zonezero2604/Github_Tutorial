I.Git là gì? là 1 dạng source control
	1.repo(repository): có thể coi là 1 project chứa toàn bộ sourcez
		+local: repo trong máy - nơi chứa code ở trong máy
			- install Git in your PC
		+remote: nằm trên máy chủ mọi người có thể pull/fetch về được. Nới chứa code trên sever được cung cấp bởi hosting service như (git,github,...)
			- Creat a Github account
		=> link Git in PC with githubt account = git config (link_local_remote.PNG)
	2.commit: khi thay đổi file là 1 commit được lưu vào repo để truy xuất
	3.branch: khi làm source code chỉ có 1 nhánh master. branch tạo 1 nhánh mới
		+Thường các công ty làm mỗi 1 lần sửa tạo 1 branch mới

II. 10 lệnh Git cơ bản Setup (setup.PNG)
	Set up 1 project với Git version control để tạo local repository trên máy tính 
	sau đó đồng bộ hóa local repository lên trên remote repository.
	Bước 1: LINK	
		1. (git) E:\forpython\git>git version
			git version 2.31.0.windows.1
		2.(git) E:\forpython\git>git config --global user.name "ZenoRePo"
			link_local_remote
		3.(git) E:\forpython\git>git config --global user.email "zonezero2604@gmail.com"
			link with github account
		4.(git) E:\forpython\git>git config --list
			user.name=ZenoRePo
			user.email=zonezero2604@gmail.com
	Bước 2:Creat Repo 
		1. Creat a local repo in your own PC chúng ta gõ lệnh git init ngay tại folder muốn tạo local repo
			(git) E:\forpython\git>git init
			Initialized empty Git repository in E:/forpython/git/.git/
