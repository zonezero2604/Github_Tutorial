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
		
	#1.Git init
		Bước 2:Creat Repo 
			1. Creat a local repo in your own PC chúng ta gõ lệnh git init ngay tại folder muốn tạo local repo
				(git) E:\forpython\git>git init
				Initialized empty Git repository in E:/forpython/git/.git/
		Bước 3: Tạo repository trên github
				đặt tên .....(Github_Tutorial)
		Bước 4: link local repo with github repo
			git remote add origin [Github_repo_URL] 
			(git) E:\forpython\git>git remote add origin https://github.com/zonezero2604/Github_Tutorial.git

	#2. Git Clone
	Clone(tải) a remote repo on Github to local PC
		git clone [Github_repo_URL] [tên folder tạo mới để bỏ các flie clone]
	b1: tạo 1 remote repo mới Github_Clone_Demo	
			tạo 1 file ms trên Github_Clone_Demo tên :clone_testing.html

	#3. Tạo 1 số file code đơn giản tại local repo trong thư mục git (index.html)
III. GitHub flow (qui trình xử lí trên git)(workflow.PNG)
	+ working directory: thư mục làm việc (E:\forpython\git) 
		ban đầu trong E:\forpython\git không có gì
	+ git init để khởi tạo git trong thư mục working directory
		tạo file index.html (có thay đổi) ---> initialization
	+git add thêm sự thay đổi vào staging area(khu vực chuẩn bị trước khi commit)
	+git commit : lưu lại các bản chụp (snapshot) của những thay đổi trong working directory
	+commit các snapshot vào trong local repository 
	+và từ local repository và {git push} lên github


		(ĐẦU CHU KỲ)
	#4 Git Add (add change to staging area) lưu thay đổi vào staging area (ĐẦU CHU KỲ)
	git add file
	git add index.html
	git add .    {add all file}
 	(git_add.PNG) từ folder working directory lưu thay đổi(index.html) vào trong staging area

	#5 Git commit lưu lại snapshots (ảnh chụp)  lưu lại các bản chụp (snapshot) của những thay đổi trong working directory commit các snapshot vào trong local repository
	git commit --m "descriptive massage" (mô tả sự thay đổi)
	git commit --m "creat a new file index.html"
	git commit --amend -m "amend descriptive massage" (thay thế mô tả mới)

	#6 Git push upload all local branch commit to github
	git push origin [branch-name]
	git push origin master

	#7 git status
	(git) E:\forpython\git>git status
	On branch master
	nothing to commit, working tree clean (nãy h đã commit xong)
		
		ví dụ thêm <span> Test git status </span>
		(git) E:\forpython\git>git status
		On branch master
		Changes not staged for commit:
		  (use "git add <file>..." to update what will be committed)
		  (use "git restore <file>..." to discard changes in working directory)
		        modified:   index.html

		no changes added to commit (use "git add" and/or "git commit -a")
		===> chưa được đưa vào staging area
	#8 git diff để xem sự thay đổi giữa các version commit với nhau
	(git diff.PNG)
	git diff 463c40c 0d9b80f

	#9 git log list ra commit mà mình đã thực hiện trên current branch
	cú pháp 1: git log-<n> //giới hạn số muốn hiển thị
				git log
	hiển thị mỗi commit trên một dòng
				git log --oneline
	#10 git reset 
	ví dụ có 1 file ở working directory lở sử dụng git add để đưa vào staging area muốn renove ra khỏi staging area
		cú pháp: git reset <tên file> 
	#11 git fetch & pull
	sychronize (đồng bộ hóa) local repository with remote repository on Github
	ex: creat 1 file ở GitHub_Clone_Demo
	 theo như "#2" thì local repo hiện tại(folder: git_clone_from_github) ko có file new_contribute_from_other_members mà trong khi trên remote repo có( nãy tạo trên GitHub)
	command: cd git_clone_from_github
		(git) E:\forpython\git\git_clone_from_github>git fetch


		(git) E:\forpython\git\git_clone_from_github>git status
		On branch main
		Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
		  (use "git pull" to update your local branch)
		  	Nó báo là local repo đang nằm sau origin repo(trên github) 1 commit

		 (git) E:\forpython\git\git_clone_from_github>git pull
		 	trong thư mục E:\forpython\git\git_clone_from_github 
		 	đã có file new_contribute_from_other_members