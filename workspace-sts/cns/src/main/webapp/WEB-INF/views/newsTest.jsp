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
				<th>���̵�</th>
				<th>����</th>
				<th>���</th>
				<th>ȸ��</th>
				<th>ī�װ�</th>
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