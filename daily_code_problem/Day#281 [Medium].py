Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:4581:b029:9e:2c6b:28d9 with SMTP id s1csp345411lkv;
        Tue, 1 Dec 2020 09:08:02 -0800 (PST)
X-Google-Smtp-Source: ABdhPJwdEomxgvOVw0cBeNVErQTceSdilPsj34T5h/mLLVqyNYS0IjkeXIeLvyfPTihVJekaEXGy
X-Received: by 2002:a37:6814:: with SMTP id d20mr3800129qkc.445.1606842482588;
        Tue, 01 Dec 2020 09:08:02 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1606842482; cv=none;
        d=google.com; s=arc-20160816;
        b=g8AtoyosTr+gAuzr+/UBKiLOCtWBXsGtsHjleYO2QTXdg8wBrWs6ZpcPbAs/0nprTk
         90OeWeKIgUfYKMsjrgbiYXK7FSfwQFw28vx7ws3EFTo9RLzhZDWei/1CGqw6cFcOqD23
         S3vs8flyc1vul8zsYOfh0K+q5qH1i6DCYOZNRgZThDkWJUvYQpqn2lU7eI/3P26MaDp6
         AuU8+dg9zKq/aNG8QlWuMuFqy/iOkOABhSaHIPQFB0aYGo9jMXQt/ASp0ShcJpfWqviL
         kZ3EqeoDDjZ4QvapAsf1UTwoELQqozdYpObLdLzT/w0AbctxLb0nn4uZMwXb8+3jLOIx
         kVmA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=FtnSy6q3TXOtSGYsE1Uqo9L7l1nRcFYnqptejm2T7bY=;
        b=V0IKXo8BLDvJ1VS2SCEeMZSkVF4EDUh7O6dnEuanog12UTcXaNlDl+ypStut3aLB+U
         fsuaPhd4W3Cy91cE5a47lcl9vmUY0t9RZtdjvpWVKQxngAIkFa11LhY37ZIaIB8TMq/8
         0K145EBzPr2nh8kxTD+nWjRTmVMfmkLmzrqEymekzqVQQ6J27wx7tQ/WzdHltJFEtf1l
         VHcbZ5deh0xmL9hD+7TXpYJIbVYKfAUOvppUSLX0MEeAOoHSfTDO+BkTSht7KFsq+laX
         OD133QFg1OYStJR4Zr3J4hugL/LNuQ90N3orcCQ1vb11g8jpasupbjyrkuz3zLaIY6j4
         xHfw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=bhYqES8w;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=NgHn9xHT;
       spf=pass (google.com: domain of 010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com
Return-Path: <010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id l17si102016qkg.149.2020.12.01.09.08.02
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Tue, 01 Dec 2020 09:08:02 -0800 (PST)
Received-SPF: pass (google.com: domain of 010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=bhYqES8w;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=NgHn9xHT;
       spf=pass (google.com: domain of 010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1606842482;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=UXM473bZV96eA8BCrGAsUHC59cYJMNcUmqtbpQ7nUGQ=;
	b=bhYqES8wfDFxASW8sj3jKXUoty3XAKDaifBjF2ZntcJZQVcsTAtswLJKp/NN0f5Y
	utF9j4BJXEIep1mPDZ/UwW4/iE7GzTdVnB4EywAKv0Q7HLXNnQPMObiZnvc1zhVEfHj
	SyYDxYgqHHw7f/nhJbQzkYZCmjTprnEWiEebNPVw=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1606842482;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=UXM473bZV96eA8BCrGAsUHC59cYJMNcUmqtbpQ7nUGQ=;
	b=NgHn9xHTbLROhLHeGVyxBgixGlJkuJUvofypbswOALZeOFT+z9P5pcU5JfGM7VSB
	XkWyX2nWA3zZVgiR/Us8ltnIMd/uwXUMHGwNXFmzA4g3YUfPOg4BBreNmxx5l39rbdT
	jzs8MVdwMpJqDUd6J+6CfV0HImaY70ORakhyAnj0=
Content-Type: multipart/alternative;
 boundary="--_NmP-a6cb12af43997812-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #281 [Medium] 
Message-ID: <010001761f467ddf-e6e69f95-40b9-410d-9c20-5faac9c8e2c1-000000@email.amazonses.com>
Date: Tue, 1 Dec 2020 17:08:02 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.12.01-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-a6cb12af43997812-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

A wall consists of several rows of =
bricks of various integer lengths and uniform
height. Your goal is to find =
a vertical line going from the top to the bottom of
the wall that cuts through the fewest number of bricks. If the line goes =
through
the edge between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row =
represent
the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]


The best we can we do here is to draw a line after the eighth brick, which =
will
only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one =
above,
return the fewest number of bricks that must be cut to create a =
vertical line.


----------------------------------------------------------=
----------------------

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
----_NmP-a6cb12af43997812-Part_1
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
    <title>Daily Coding Problem: Problem #281 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">A wall consists of several=
 rows of bricks of various integer lengths and uniform height. Your goal is=
 to find a vertical line going from the top to the bottom of the wall that =
cuts through the fewest number of bricks. If the line goes through the edge=
 between two bricks, this does not count as a cut.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, suppose the input is as =
follows, where values in each row represent the lengths of bricks in that =
row:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid =
#cccccc; font-size: 13px; line-height: 19px; overflow: auto; padding: 6px =
10px; border-radius: 3px;"><code class=3D"lang-python" =
style=3D"border-radius: 3px; font-family: monospace; margin: 0; padding: 0;=
 white-space: pre; background: transparent; background-color: transparent; =
border: none;">[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
</code></pre>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">The best we can we do here is to draw a line after the eighth =
brick, which will only require cutting through the bricks in the third and =
fifth row.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given an input consisting =
of brick lengths for each row such as the one above, return the fewest =
number of bricks that must be cut to create a vertical line.</p>
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
----_NmP-a6cb12af43997812-Part_1--
