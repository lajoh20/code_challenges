Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:3618:0:0:0:0 with SMTP id q24csp593918ejb;
        Fri, 7 Aug 2020 08:50:30 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzT6BRTr15OHkVG1U/Dl4Gz7EJm7sJsM+TpddyfhnQXrdSaekzAzHnd9o1elcEs8j/5O1lh
X-Received: by 2002:a05:620a:234:: with SMTP id u20mr13700525qkm.54.1596815429954;
        Fri, 07 Aug 2020 08:50:29 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1596815429; cv=none;
        d=google.com; s=arc-20160816;
        b=agM9HwZf1B/xG9rRqJ5tvEqhGyybZPViiaXxHydOjrvkbgRr+TewhX/E7VYY5GY6fW
         MTPFBM+rKNZIbr00XCemqQ50QHMk7WHV8Br6pILGq/OR5N1K9MsbzWfz7TKQlsUv3id8
         bxfa1H2zs4XbEgUoTw7bOlS1YVA2tleLyNGZKacd54yRmn7VTxTUej1LS33yI+g3dLAI
         hRoWjMTPCmXaj53PUr9pUM3amqwN2iSczcf/TRDB48zwM7uvIXAScyN8V1dAbpqofYLI
         5Vz3VifHZNL4cuyUVoQpRAiOrFGqA9yUWLipy4Fqy5UuNxAbmaZ0zXCV466jnUZwSh+/
         KzdQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Y7jjitg8ksQe6DXlxV1UOSKy8NQztsAZ/OEQvpM7XHU=;
        b=ES7NyZUZUcRQ3IND/KZzW/EewTw6nSkXVKd7NL86kSLaHFaD00ckPGouJDcAButauy
         TwxLgisQ4pa+tMWJWGL4b3/hh1N2OJ7n7XFkHzYZk2e7TmnCI2zCAuo4EqjB3MU4zPLv
         SCo3hVV+iMX3nfsj9K7Iv99VI+98aJCEmSIC84YZViqnXXaD+ZBYu/NY+BVWYv68VRka
         4sGc2Lo6PelRqRlvmDL/AdD4nrQXmTHiGEVTzOdxUkuCzpqIRNchwv50da3XEmAtC7CP
         Clzrg0kYlZvBo/7sjL6Z+ipTf6sP+5M4G64ZGpSPLgEofBV0/7FmtsfMZhdzxDtsV3f2
         KQtw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=EAm4gsxR;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b="Da7k/JVy";
       spf=pass (google.com: domain of 01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com
Return-Path: <01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id h13si5120208qtp.34.2020.08.07.08.50.29
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 07 Aug 2020 08:50:29 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=EAm4gsxR;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b="Da7k/JVy";
       spf=pass (google.com: domain of 01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1596815429;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=R4dtfE5pl7jZVpM0NELb2+Suzzn9dj3pB3THVK00pww=;
	b=EAm4gsxRr3Sfm1Wph1R4DQ2XHEHjjuqoG/Z57UPaTyJheJ8Ov+qOHmbKIbWpzQZy
	VT62dAraeKviI3CziKUXfbQk5XZ7WAODjnLgoUUduAzyvS+k4F2HlUxRzi+x+9d0l0u
	hjgwnu28l7K0M+yHmF10/e+BN7nRepm+423FtGGo=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1596815429;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=R4dtfE5pl7jZVpM0NELb2+Suzzn9dj3pB3THVK00pww=;
	b=Da7k/JVyKYnviiZVjQLeCuJAM4fjZyYlpB4t5kH8hj020i/dkk80ftFX4713k0/k
	mEUb9d+etC/dH6y2rOw9MMCr5qy909bGrbRkcIx0H3wJy2QmkhsrdF2wbmMb6YmNp9x
	bqTjoSpQXvfC6h7gcxACLbqTzrdkrl9TpatWYYkg=
Content-Type: multipart/alternative;
 boundary="--_NmP-30675dcd09790290-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #166 [Medium] 
Message-ID: <01000173c99dcda5-65408300-1e50-4497-96d2-82455abca13e-000000@email.amazonses.com>
Date: Fri, 7 Aug 2020 15:50:29 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.08.07-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-30675dcd09790290-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Implement a 2D iterator class. It will be =
initialized with an array of arrays,
and should implement the following =
methods:

 * next(): returns the next element in the array of arrays. If =
there are no more
   elements, raise an exception.
 * has_next(): returns =
whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling =
next()=20
repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be
empty.


------------------------------------------------------------------=
--------------

Upgrade to premium
[https://www.dailycodingproblem.=
com/subscribe?email=3Dlewisjohnson1066334%40gmail.com]=20
and get in-depth solutions to every problem, including this one.=20

If you liked this problem, feel free to forward it along so they can =
subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot us =
an email if
there's anything we can help with!


--------------------------=
------------------------------------------------------

Master algorithms together on Binary Search [https://binarysearch.io/?=
ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-30675dcd09790290-Part_1
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.=
w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=3D"http://www.w3=
.org/1999/xhtml">
  <head>
    <meta name=3D"viewport" =
content=3D"width=3Ddevice-width, initial-scale=3D1.0">
    <meta http-equiv=3D"Content-Type" content=3D"text/html; =
charset=3DUTF-8">
    <title>Daily Coding Problem: Problem #166 [Medium]
</title>
    <style type=3D"text/css" rel=3D"stylesheet" media=3D"all">
@media only screen and (max-width: 600px) {
  .email-body_inner,
.email-footer {
    width: 100% !important;
  }
}
@media only screen and =
(max-width: 500px) {
  .button {
    width: 100% !important;
  }
}
</style>
  </head>
  <body style=3D"height: 100%; margin: 0; line-height: 1.4; =
background-color: #F2F4F6; color: #74787E; -webkit-text-size-adjust: none; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box; width: 100%;">
    <table class=3D"email-wrapper" =
width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; background-color: =
#F2F4F6;" bgcolor=3D"#F2F4F6">
      <tr>
        <td align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
          <table =
class=3D"email-content" width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 100%; margin: 0; padding: 0; =
-premailer-width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: =
0;">
            <table class=3D"email-head_inner" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0;">
              <tr>
                <td class=3D"email-masthead" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 25px 35px; height: 30px; vertical-align: =
middle; border-collapse: collapse;" height=3D"30" valign=3D"middle">
                  <a href=3D"https://www.dailycodingproblem.com/" =
class=3D"email-masthead_logo_link" style=3D"color: #3869D4; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; vertical-align: middle; text-decoration: none; =
padding: 0; margin: 0; display: inline-block;">
                    <img =
class=3D"email-masthead_logo" src=3D"https://www.dailycodingproblem.=
com/static/icon-round.png" width=3D"30" height=3D"30" style=3D"font-family:=
 Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; border: 0; vertical-align: middle;">
                  </a>
                  <a href=3D"https://www.=
dailycodingproblem.com/" class=3D"email-masthead_link" style=3D"color: =
#3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; height: 30px; vertical-align: middle; padding-left:=
 6px; text-decoration: none;">
                    <span =
class=3D"email-masthead_name" style=3D"font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box; font-size: 14px; =
font-weight: bold; color: #343434; text-decoration: none; text-shadow: 0 =
1px 0 white; height: 50px;">Daily Coding Problem</span>
                  </a>
                </td>
              </tr>
            </table>
            <!-- Email Body -->
            <tr>
              <td class=3D"email-body" width=3D"100%" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; width: =
100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; border-top: 1px solid=
 #EDEFF2; border-bottom: 1px solid #EDEFF2; background-color: #FFFFFF;" =
bgcolor=3D"#FFFFFF">
                <table class=3D"email-body_inner" =
align=3D"center" width=3D"570" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 570px; margin: 0 auto; padding: 0; =
-premailer-width: 570px; -premailer-cellpadding: 0; -premailer-cellspacing:=
 0; background-color: #FFFFFF;" bgcolor=3D"#FFFFFF">
                  <!-- Body content -->
                  <tr>
                    <td class=3D"content-cell" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 35px;">
											<p style=3D"margin-top:=
 0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Good morning! Here&#39;s your coding interview problem for =
today.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">This problem was asked by =
Uber.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Implement a 2D iterator =
class. It will be initialized with an array of arrays, and should implement=
 the following methods:</p>
<ul style=3D"text-align: left; color: #555; =
font-size: 16px; line-height: 1.5em; padding-left: 24px; font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;"><code style=3D"font-family: monospace; margin: 0 =
2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">next()</code>: returns the =
next element in the array of arrays. If there are no more elements, raise =
an exception.</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;"><code style=3D"font-family:=
 monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px=
 solid #eaeaea; background-color: #f8f8f8; border-radius: =
3px;">has_next()</code>: returns whether or not the iterator still has =
elements left.</li>
</ul>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, given the input [[1, 2], [3], [], [4, 5, 6]], calling <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">next()</code> repeatedly should output <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">1, 2, 3, 4, 5, 6</code>.</p>
<p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Do not use <code style=3D"font-family: monospace; margin: 0 =
2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">flatten</code> or otherwise=
 clone the arrays. Some of the arrays can be empty.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><a =
href=3D"https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Upgrade to premium</a> and get in-depth solutions to every =
problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">If you =
liked this problem, feel free to forward it along so they can <a =
href=3D"https://www.dailycodingproblem.com/" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">subscribe here</a>! As always, shoot us an email if =
there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Master algorithms together on <a =
href=3D"https://binarysearch.io/?ref=3Ddcp" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Binary Search</a>. Create a room, invite your friends, and =
race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica=
 Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; line-height: 1.5em; text-align: =
left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; font-size: 0.7em;">
  No more? <a =
href=3D"https://dailycodingproblem.com/unsubscribe?unsubscribeKey=3D15bb434=
5a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de658c7d6d6b960ec" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Snooze or unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td style=3D"word-break: break-word; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
                <table class=3D"email-footer" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" =
align=3D"center" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; padding: =
35px;">
                      <p class=3D"sub align-center" =
style=3D"margin-top: 0; line-height: 1.5em; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box; text-align: center; =
color: #AEAEAE; font-size: 12px;">&copy; 2019 Daily Coding Problem. All =
rights reserved.</p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
----_NmP-30675dcd09790290-Part_1--
