Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:76c2:0:0:0:0 with SMTP id q2csp1586782ejn;
        Thu, 23 Jul 2020 08:45:23 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJznkWmrXMSoe4IJ4ORgoruPW1NVbc1GkYaUxGIJ6KBL2DW7/9iYTdb+Y4kc1KafGQPdGDst
X-Received: by 2002:a37:bac2:: with SMTP id k185mr5433808qkf.425.1595519123321;
        Thu, 23 Jul 2020 08:45:23 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1595519123; cv=none;
        d=google.com; s=arc-20160816;
        b=fu8EL+abFBt6YRxHfCQcqIixNPC0hFl1/xTSr4eYGQUpgso+yoE/5/qdbr2jGWxxD0
         zNfYhGnz0RnHh4cg6f7lNqg0XDd9TOjawxGAqaupUzOv+uqCFNCzvoT/IdvA9Qkvqqyf
         7iKogxbFMguM08Vrxh+/kst6Ni6I/f+2pr79A61wLUOE+SAfirewLUebiRNJxv5mmpAw
         7F9SCAOPKwtOwuIZIFHNXk1PK51fPxHcP51aA3DEreNyriSqcRXI8srfBhnV4rAhjxHz
         fqA2ZYs13cVa+sK+XdX2KaVTwyF9w5QmX1XcROk6RksQSCllI/aCCyym3sdrmiZ31HLn
         A+Vw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=shf/PD+7MbaR/aBWkniwtPMB+d+PRLOGzMowd1cMLcA=;
        b=fzohG5e8f5isVV6wVVpxlWM26Ajo9Fe0pKGSbTGdV7mnU8JKZzoSqnkFCS/+Hv+FxG
         EJLtlb2BPzDeG1SC/OuJRG5YbWZsVhIdeEtqGjIrUstPSVWbMFCZm8R1OCTuMmCQPV16
         6UyJbplsnEONkdeXxo+27CiTPz8n4iR1EYJ2B3NkaQySmFNgZRv1dozqST8RoG/M7+Cs
         gtz0jpopkTjwQgXCR3hbYXUvUrY6t+zBo6DBD9zZnoih9moRWjVTGnrOCAb0VR0Q6Buh
         bSX8e32CLHmWx9uYh3aeb+qWGgvc5gv0mpUtn22lOKfsD1zvZfeF45SMFyK3fVtBXxhW
         vzig==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Z9F7VAtM;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=QDFNnGBp;
       spf=pass (google.com: domain of 010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com
Return-Path: <010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id w24si1725771qkf.179.2020.07.23.08.45.23
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 23 Jul 2020 08:45:23 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Z9F7VAtM;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=QDFNnGBp;
       spf=pass (google.com: domain of 010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1595519122;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=mcelVIuBxW4TJr1Dm2B/JOly7tjPM0F+FNfjJ2x48cM=;
	b=Z9F7VAtMSU5VUOg87Lpu6pTHOqbtnHPw7VhcrWwWVDnm0JqxxDysw7sgK8IrEg7Y
	jMxBx8fGiCHb7UwVUCOjbZH+eNQgtVu5T8JgwDdVlN0thkR0cKuTVx91hAcqUSgzQ0a
	BZwh6iCK7IHevzn7eQwt+z1ugGiS9wP/7tdiyrTE=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1595519122;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=mcelVIuBxW4TJr1Dm2B/JOly7tjPM0F+FNfjJ2x48cM=;
	b=QDFNnGBpW0z3E8u9x3GKIqmNNAoYF6BS8cEgsdcFg6hgG/DuDIdX1GwL5l8Bg+TF
	bXoWsgU9siTxCJ9YtWFaWgCd7K8C8b1tqPr4NyJ2dckUA5l7/Ua2FjKX2xQp4LXeNym
	9EV8dacXlvXug6Pe1iv6Yu2ERnjYc3jNPJRMjzPU=
Content-Type: multipart/alternative;
 boundary="--_NmP-59b60dadec7833af-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #151 [Medium] 
Message-ID: <010001737c59bda2-a677647a-f517-4192-976c-05b86165bc13-000000@email.amazonses.com>
Date: Thu, 23 Jul 2020 15:45:22 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.23-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-59b60dadec7833af-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

Given a 2-D matrix representing an image, a location of a pixel in the =
screen
and a color C, replace the color of the given pixel and all adjacent=
 same
colored pixels with C.

For example, given the following matrix, and =
location pixel of (2, 2), and 'G'
for green:

B B W
W W W
W W W
B B B


Becomes

B B G
G G G
G G G
B B B



---------------------------------------=
-----------------------------------------

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%4=
0gmail.com]=20
and get in-depth solutions to every problem, including this =
one.=20

If you liked this problem, feel free to forward it along so they =
can subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot =
us an email if
there's anything we can help with!


---------------------------------------------------------------------------=
-----

Master algorithms together on Binary Search [https://binarysearch.=
io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-59b60dadec7833af-Part_1
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
    <title>Daily Coding Problem: Problem #151 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given a 2-D matrix =
representing an image, a location of a pixel in the screen and a color =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">C</code>, replace the color of the given pixel and all=
 adjacent same colored pixels with <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">C</code>.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the following =
matrix, and location pixel of (2, 2), and &#39;G&#39; for green:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">B B W
W W W
W W W
B B B
</code></pre><p style=3D"margin-top: 0; color: #555; font-size:=
 16px; line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica=
 Neue', Helvetica, sans-serif; box-sizing: border-box;">Becomes</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">B B G
G G G
G G G
B B B
</code></pre><hr style=3D"font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;"><a href=3D"https://www.dailycodingproblem.com/subscribe?=
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
----_NmP-59b60dadec7833af-Part_1--
