<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<head>

<meta charset="utf-8">
<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">

<!-- Bootstrap core CSS -->
<link href="/resources/vendor/bootstrap/css/bootstrap.min.css"
	rel="stylesheet">

<!-- Custom styles for this template -->
<link href="/resources/css/modern-business.css" rel="stylesheet">
<link href="/resources/css/ij-css.css" rel="stylesheet">
<title>QuadCore News</title>

</head>


<body class="bg-light">

	<nav class="navbar fixed-top navbar-expand-lg navbar-dark fixed-top"
		style="background-color: #A566FF">
		<div class="container">
			<a class="navbar-brand" href=".do">QuadCore News</a>
		</div>
	</nav>



	<!-- Page Content -->
	<div class="container" style="padding-top: 30px;">
		<div
			class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow"
			style="background-color: #343a40">
			<img class="mr-3" src="img/user.png" alt="" width="48" height="48">
			<div class="lh-100">
				<h6 class="mb-0 text-white lh-100">MyPage</h6>
				<a class="mb-0 text-white lh-100" href="/alert/logout"><small>로그아웃</small></a>
			</div>
		</div>

		<div class="my-3 p-3 bg-white rounded box-shadow">
			<h6 class="border-bottom border-gray pb-2 mb-0">내가 스크랩한 뉴스</h6>
			<c:forEach items="${newsList}" var="news" begin="0" end="3" step="1">
			<div class="media text-muted pt-3">
				<img
					data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1"
					alt="" class="mr-2 rounded">
				<p
					class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
					<strong class="d-block text-gray-dark">${news.news_title}</strong> ${news.date_of_news}
				</p>
			</div>
			</c:forEach>
			
			<small class="d-block text-right mt-3"> <a href="#">더보기</a>
			</small>
		</div>

		<div class="my-3 p-3 bg-white rounded box-shadow">
			<h6 class="border-bottom border-gray pb-2 mb-0">나의 태그</h6>
			<div class="media text-muted pt-3">
				<p
					class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
					<c:forEach items="${tagList}" var="tag" begin="0" end="3" step="1">
					<span># ${tag.tag_content}</span>
					</c:forEach>
				</p>
			</div>
			<small class="d-block text-right mt-3"> <a href="#">수정하기</a>
			</small>
		</div>

<!-- 		<div class="my-3 p-3 bg-white rounded box-shadow">
			<h6 class="border-bottom border-gray pb-2 mb-0">회원정보</h6>
			<div class="media text-muted pt-3">
				<img
					data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1"
					alt="" class="mr-2 rounded">
				<p
					class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
					<strong class="d-block text-gray-dark">이름</strong> 김**
				</p>
			</div>
			<div class="media text-muted pt-3">
				<img
					data-src="holder.js/32x32?theme=thumb&bg=e83e8c&fg=e83e8c&size=1"
					alt="" class="mr-2 rounded">
				<p
					class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
					<strong class="d-block text-gray-dark">생년월일</strong> ****년 **월 **일
				</p>
			</div>
			<div class="media text-muted pt-3">
				<img
					data-src="holder.js/32x32?theme=thumb&bg=6f42c1&fg=6f42c1&size=1"
					alt="" class="mr-2 rounded">
				<p
					class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
					<strong class="d-block text-gray-dark">주소</strong> 서울특별시 도봉구 삼양로144
					33길
				</p>
			</div>
			<small class="d-block text-right mt-3"> <a href="#">수정하기</a>
			</small>
		</div>
 -->

	</div>


	  <!-- Bootstrap core JavaScript -->
    <script src="/resources/vendor/jquery/jquery.min.js"></script>
    <script src="/resources/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
</body>
</html>
