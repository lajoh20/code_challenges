Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:76c2:0:0:0:0 with SMTP id q2csp651899ejn;
        Wed, 22 Jul 2020 08:46:41 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJxrooZJBn+hnV4x7Xi++eUBsEBPbeRpNETvdb5hOFMQbnvV3vYA/rj2da/FaQnC2e9kjx7M
X-Received: by 2002:ad4:510e:: with SMTP id g14mr567464qvp.111.1595432801422;
        Wed, 22 Jul 2020 08:46:41 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1595432801; cv=none;
        d=google.com; s=arc-20160816;
        b=SzVQK7xWKeYCfkBiOPWVVihzWNXU7J46Ss5FYqPpRPE8P+sdq6H1jh4E1ujav241Yq
         0/WGpNdZDWkkAQ7EeqNnAwFuLzeAOPOOwADbXgf1544Kvn58PjsEApjduJT1K/tx6FyQ
         WL3UioQQNNzb9wjeGf0RojK67Op23n2yDohCn9/IID1MOjgnnq5JDwpli4W11zyC4bX3
         cYTwc6NW5CZSkkCC604SSTSnaEe8Wp7tQCPi1TFQyugytEG6U0k3dtDorZrgPaI/mbZ8
         yBufqM0qxrTCnHbyym2QSKqE8boBhjepahOplT8bf7ef3J5UlaRF2Odi2r9u98O41Tuu
         zzwQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=AvK8M+2tVcxbaBYHdPRw7EuM/sTFT+y8+Dg6RbJn664=;
        b=Y0A1iI2EhkYXm3XTaiJ3VWnWnxZLzwgJ2xeUwTjjHSc6pMQOJFonSYcBZHJ5lvLwnl
         aDRbF551PWF8HqQk3j+UnlmbBKfDnjGSQqKx/x2TusDNY3+dfwPRM6CNxMrnNuFH8a+H
         0AtRTDJQRlbt3J7K4JJ9PkArFpNMm4hKoa7iBDeZiZaL7qHLT+NZ+NeezzBhOPWL7bC3
         0IS4CD87vdInowhsgtm4PInseORl3Z5kHvUCxh38KomuT4tnLaXKY8N5uhFDFOleWZw9
         GIri6kxMySRkzV/ZbmX/WPMM9WZu7WfD5JgOh9HXnlA2Rox1EP7/NzXeR5nnMBL4E1ot
         eZzw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=K4jFBDm6;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=jmYZ+IOD;
       spf=pass (google.com: domain of 01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com
Return-Path: <01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id t10si9023qtb.368.2020.07.22.08.46.41
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Wed, 22 Jul 2020 08:46:41 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=K4jFBDm6;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=jmYZ+IOD;
       spf=pass (google.com: domain of 01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1595432801;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=Bqc2DoI1BROPtwpnEefi1PRX4rEL209/EqwzmJe+IHU=;
	b=K4jFBDm62avckP2LOcRU8gqOGTkrnMNUh7SoWOT0LG+sT25s6493jNeVZAkZlSCi
	uQQK24XXG5LXmw0QxOepEkwCNSJ3evXyVHnRtsov0LmkYOdNZTzxZCZy95um58N1CkX
	Mz0i+6NsT7C4b00Jy5HQYBDZ7RiUWys768g/XyZs=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1595432801;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=Bqc2DoI1BROPtwpnEefi1PRX4rEL209/EqwzmJe+IHU=;
	b=jmYZ+IOD2upsssX1y5BOt3uAbeI7ezWBLQtmXdQxcp+9FdMN5UJ2XzWCB0leQ30u
	AtzH6jb3eY7Y5XbrTRmD4FMMyK8hOslBACx/KFOe1Ii7KKDv4Xtw3CzefWIWqdpjnWm
	YnHPeitnfe3GM/O5STWP2itFKY7x2MZ9vm1NCC7A=
Content-Type: multipart/alternative;
 boundary="--_NmP-f425f63cb4517deb-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #150 [Hard] 
Message-ID: <01000173773492ba-5c500601-c8bc-487d-8ef0-1b8f29b4c4ff-000000@email.amazonses.com>
Date: Wed, 22 Jul 2020 15:46:40 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.22-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-f425f63cb4517deb-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a list of points, a central =
point, and an integer k, find the nearest k=20
points from the central =
point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the=
 central
point (1, 2), and k =3D 2, return[(0, 0), (3, 1)].


---------------------------------------------------------------------------=
-----

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com]=20
and get in-depth solutions to =
every problem, including this one.=20

If you liked this problem, feel free=
 to forward it along so they can subscribe
here [https://www.=
dailycodingproblem.com/]! As always, shoot us an email if
there's anything we can help with!


--------------------------------------=
------------------------------------------

Master algorithms together on =
Binary Search [https://binarysearch.io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the problem!


---------------------------------------------------------------------------=
-----

No more? Snooze or unsubscribe
[https://dailycodingproblem.=
com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f=
89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-f425f63cb4517deb-Part_1
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
    <title>Daily Coding Problem: Problem #150 [Hard]
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
LinkedIn.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a list of points, a =
central point, and an integer <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">k</code>, find the=
 nearest <code style=3D"font-family: monospace; margin: 0 2px; padding: 0 =
5px; white-space: nowrap; border: 1px solid #eaeaea; background-color: =
#f8f8f8; border-radius: 3px;">k</code> points from the central point.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the list of points =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">[(0, 0), (5, 4), (3, 1)]</code>, the central point =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">(1, 2)</code>, and <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">k</code> =3D=
 2, return
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0=
 5px; white-space: nowrap; border: 1px solid #eaeaea; background-color: =
#f8f8f8; border-radius: 3px;">[(0, 0), (3, 1)]</code>.</p>
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
----_NmP-f425f63cb4517deb-Part_1--
