Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1dd1:0:0:0:0 with SMTP id v17csp492713ejh;
        Sat, 9 May 2020 08:43:26 -0700 (PDT)
X-Google-Smtp-Source: APiQypIG0LMXu2S1PtOPbTIJbbngKoYLWkXInSvON2aQPh5E4+7dYXPsmxmUI+2JrSDRH21hWH+b
X-Received: by 2002:ac8:3664:: with SMTP id n33mr8945482qtb.363.1589039006139;
        Sat, 09 May 2020 08:43:26 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1589039006; cv=none;
        d=google.com; s=arc-20160816;
        b=K0L/RXyL7qigWGJhYXHgOa7CLy+CG/632WMEioyTOEFny51v+M/D77uLT6w11mDenA
         Nw0xOzybqha6ossK1hlG1OlExR8X/+zspejM9KjqTyDqlderWUQLiXT8v7Q9MEieF4WH
         /jPbuSPWCgsxygXqQSV3jYw5YetlyUfGjAI6GHOeOhU8TcthiMR0Tt1dT3XtgbEnT7K/
         TQhiceMspZ4avAn06z+R8R4MpiTtq9SXCvQoMtpExw87b1+bJ2c52bDgRoDZ05E0mtMl
         ghe8iv6/6mEPqHCnG/eTbAoi7ZZ7x7FGR01OP3j0CMWaXXeOj/vpZY2VzgQnOrfAhBFi
         Czvw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=zqNofhViWkH7Bi+lBb8DhwRjek2D9flLUlldT8d/aBM=;
        b=qNdXrSdilP/nJrBVZkAmbpDNt3k+WQ/YjloWfOtaln7xm3L50r/470JXj51nphJw0s
         OEqonGkSJJttgxAHwOTrHGTm8kk3Byo6ydm4E1oc/GKp4umL3Zgls0kF6A3b6/rLpYkQ
         OPDnVN7KNNaNicvEOShDwWOucKG0gf9T5fUiClBYTl/LgOahGBfAbATgYWIe7DS/a3+I
         MNZV+J+XCfkDLBLZNcP0DrvbQj3QAuOIr1BJwTterjlUqXm+oO+4Gap55VxSF0ZWv8Ae
         WbCq16RDZXYnxAjq65ANl6UOPSLkLBUiO5pA3bk7TxuKu+1usMVuRCRjz3e/qTUilsSu
         95Ww==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=e4VjJ+c4;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=I+hRpqzq;
       spf=pass (google.com: domain of 01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com
Return-Path: <01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id ba18si2924106qvb.198.2020.05.09.08.43.25
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sat, 09 May 2020 08:43:26 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=e4VjJ+c4;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=I+hRpqzq;
       spf=pass (google.com: domain of 01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1589039005;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=7+B9UnhbJZEv1SkBDki+wmjpDRP9K350Cfvztm0EJZc=;
	b=e4VjJ+c4vHes3VB7lBFbRXM74IlGi39bh7tIPvM36yVJqlvOcTkoLXoPaxMa28zP
	mKB5qYUTYbZWTwpDM4YAJ+wh64gIN8TYuIzaDwIZUi3t5zhyvOwIiklnOeC5e0NpZnB
	b474J4rEy9w/rvGQ+SwMdS3tr0qu9HlP78JtTlKA=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1589039005;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=7+B9UnhbJZEv1SkBDki+wmjpDRP9K350Cfvztm0EJZc=;
	b=I+hRpqzqEmEQqSnctFuR29lwm6rxZihm2sdloDhuDxU5hP7Wb4rJ3N1Ke5DA8Lhx
	mLUX/yjRq3x7SazORzWvUXkzIEoliV6KBGNWrEGq48f9HVoBasmMURHqpRK0HtjgdXn
	zdgJBITu9+ZqPBOHguAZdGKRq67d6uP8tKfFyLvk=
Content-Type: multipart/alternative;
 boundary="--_NmP-73bef22c85723cf0-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #76 [Medium] 
Message-ID: <01000171fa1aff0d-a855b05f-cd37-41d2-91d4-3c78791c0566-000000@email.amazonses.com>
Date: Sat, 9 May 2020 15:43:25 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.05.09-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-73bef22c85723cf0-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an N by M 2D matrix of =
lowercase letters. Determine the minimum
number of columns that can be =
removed to ensure that each row is ordered from
top to bottom =
lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether=
 each
row itself is ordered lexicographically.

For example, given the =
following table:

cba
daf
ghi


This is not ordered because of the a in the=
 center. We can remove the second
column to make it ordered:

ca
df
gi


So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef


Your function should return 0, since the rows are already ordered (there's =
only
one row).

As another example, given the following table:

zyx
wvu
tsr


Your function should return 3, since we would need to remove all the =
columns to
order it.


----------------------------------------------------=
----------------------------

Upgrade to premium
[https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.=
com]=20
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
----_NmP-73bef22c85723cf0-Part_1
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
    <title>Daily Coding Problem: Problem #76 [Medium]
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
Google.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">You are given an N by M 2D=
 matrix of lowercase letters. Determine the minimum number of columns that =
can be removed to ensure
that each row is ordered from top to bottom =
lexicographically. That is, the letter at each column is lexicographically =
later
as you go down each row. It does not matter whether each row itself =
is ordered lexicographically.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, given the following table:</p>
<pre style=3D"background-color: =
#f8f8f8; border: 1px solid #cccccc; font-size: 13px; line-height: 19px; =
overflow: auto; padding: 6px 10px; border-radius: 3px;"><code =
style=3D"border-radius: 3px; font-family: monospace; margin: 0; padding: 0;=
 white-space: pre; background: transparent; background-color: transparent; =
border: none;">cba
daf
ghi
</code></pre><p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">This is not ordered because of the a in the center. We can =
remove the second column to make it ordered:</p>
<pre =
style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; font-size: =
13px; line-height: 19px; overflow: auto; padding: 6px 10px; border-radius: =
3px;"><code style=3D"border-radius: 3px; font-family: monospace; margin: 0;=
 padding: 0; white-space: pre; background: transparent; background-color: =
transparent; border: none;">ca
df
gi
</code></pre><p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">So your function should return 1, since we only needed to =
remove 1 column.</p>
<p style=3D"margin-top: 0; color: #555; font-size: =
16px; line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">As another example, =
given the following table:</p>
<pre style=3D"background-color: #f8f8f8; =
border: 1px solid #cccccc; font-size: 13px; line-height: 19px; overflow: =
auto; padding: 6px 10px; border-radius: 3px;"><code style=3D"border-radius:=
 3px; font-family: monospace; margin: 0; padding: 0; white-space: pre; =
background: transparent; background-color: transparent; border: =
none;">abcdef
</code></pre><p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Your =
function should return 0, since the rows are already ordered (there&#39;s =
only one row).</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px;=
 line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box;">As another example, given=
 the following table:</p>
<pre style=3D"background-color: #f8f8f8; border: =
1px solid #cccccc; font-size: 13px; line-height: 19px; overflow: auto; =
padding: 6px 10px; border-radius: 3px;"><code style=3D"border-radius: 3px; =
font-family: monospace; margin: 0; padding: 0; white-space: pre; =
background: transparent; background-color: transparent; border: none;">zyx
wvu
tsr
</code></pre><p style=3D"margin-top: 0; color: #555; font-size: =
16px; line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">Your function should=
 return 3, since we would need to remove all the columns to order it.</p>
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
----_NmP-73bef22c85723cf0-Part_1--
