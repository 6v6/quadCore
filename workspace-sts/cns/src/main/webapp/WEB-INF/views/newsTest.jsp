<%@ page language="java" contentType="text/html; charset=EUC-KR"
	pageEncoding="EUC-KR"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
<meta charset="EUC-KR">
<title>News</title>
</head>
<body>
	<h1>My News List!</h1>

	<table>
		<thead>
			<tr>
				<th>아이디</th>
				<th>제목</th>
				<th>기사</th>
				<th>회사</th>
				<th>카테고리</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach items="${newsList}" var="news">
				<tr>
					<td>${news.id}</td>
					<td>${news.title}</td>
					<td>${news.article}</td>
					<td>${news.company}</td>
					<td>${news.category}</td>
				</tr>
			</c:forEach>
		</tbody>
	</table>
</body>
</html>