Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp1205208ejc;
        Tue, 7 Jul 2020 08:44:06 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJz9mopsd/zStGPUXrEpD7kDp3+VhHFxtlzhKbXU3ELW6Nfuz2xZ0dJ8483qTYJdiMSNGEKi
X-Received: by 2002:a05:620a:1674:: with SMTP id d20mr44724890qko.131.1594136646584;
        Tue, 07 Jul 2020 08:44:06 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1594136646; cv=none;
        d=google.com; s=arc-20160816;
        b=h/QVFMbyIUooI+VyypvI3Sa6yQ01+XXZ2rTrA4+KV3DahGY10w18Huc954yhOfd7xd
         PkvWyZJJ7GL0851Jzg1p+7+S/Ps9fP/BdV0CHXznBO1j7fL+/sj6Y11dhOrFwjfdUrfh
         dMPX7IclmSrBlOeMPgbwOdfmQowGH6Bel/RuodcZGPf4D/+3uR6g0PUtZVPOaI8Jw4Zt
         pgfOLz7WynKSYxlxe8FPE3w2VACz5EDaBKX0TFCA+niB7DgF8hdSYfrcmwGgEsrxQrEq
         XDmpl1B38667hWnNrOfo7BotHDzDQE+eykZuixUBeyQmGK5KDGC1kGqEnO0Gfu/rFakO
         vTqw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Agv/39PuiP/ODspj0rdb4RdHNQSEySv1i8Cp2hp3qlg=;
        b=AwVn+jISYy2lcfqjW5QmAncFyZK4PoPS78imTUTeYDqpqkFde/0IZlrPecjeMEHdne
         AX5bOsFCqfKvxGYpaGkNhIiXZXRM17XCw3YRG3EK5GR9D3FXEabnFvNaU5nXyFls3p6p
         T7r7LqZFvwKYSg2AP4GN+LTa5TUGxn0JWub6ImzghrhcwxKMQfr8bW1uQQc2Qhl4UkiC
         rR/tCxGvF4A938e2Ok9xIzH2gm/SY0UQtMbDfkcbRHQhvyUL5kg8+yZmurWoFr2ssjaV
         Ia8zffou40RVylbZJV1IOkF//9LziX10fLetEF7/HYjGA/mhWSu7PWXGxb6SRg/Iav0N
         MN1Q==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=XE8AYXEu;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=ejFY9BIj;
       spf=pass (google.com: domain of 0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com
Return-Path: <0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id m13si13417246qth.291.2020.07.07.08.44.06
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Tue, 07 Jul 2020 08:44:06 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=XE8AYXEu;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=ejFY9BIj;
       spf=pass (google.com: domain of 0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1594136646;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=fT58dP/RO4butFh+oSLFEx/Z6RPHqWw4JhMzDZPyYcQ=;
	b=XE8AYXEuPy3rX50d/fflZngKNMOHc84Ecd3wq3cqhIZCsHsjuvJy8aQ503ujDm5y
	g+0YL31BvBAAoMWXxxqFFZ0MmVzId6n+JNAipA+bKCsJhxOQFzp3owqaC1W2PTlK5ra
	ByOKxNfXIDJ+XWJ6/XFq0blKpKaw/6e/4fA/LXa4=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1594136646;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=fT58dP/RO4butFh+oSLFEx/Z6RPHqWw4JhMzDZPyYcQ=;
	b=ejFY9BIjcrHMrCNXYi8Y19wEolcgz8kcdAIDu9554cv3gOjrY1HY5UYGxogVfngc
	WFM3db/blwvyYB3EosgD8Xt4QWHyHB8l9mrqTnzHvzMTV/gYkdXVvETTAV3Y9cNjZuL
	7FGRjP7BkeQJzUO0DvM16b9uetSzOGT1y7PEO3LY=
Content-Type: multipart/alternative;
 boundary="--_NmP-bed177143eb38bee-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #135 [Easy] 
Message-ID: <0100017329f2d03a-15961c83-6221-4665-9b7f-f304cda8d962-000000@email.amazonses.com>
Date: Tue, 7 Jul 2020 15:44:05 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.07.07-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-bed177143eb38bee-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This question was asked by Apple.

Given a binary tree, find a minimum path=
 sum from root to a leaf.

For example, the minimum path in this tree is =
[10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1



-------------------------------------------------------=
-------------------------

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
----_NmP-bed177143eb38bee-Part_1
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
    <title>Daily Coding Problem: Problem #135 [Easy]
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
 Helvetica, sans-serif; box-sizing: border-box;">This question was asked by=
 Apple.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a binary tree, find =
a minimum path sum from root to a leaf.</p>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For example, the minimum path in this tree is [10, 5, 1, -1], =
which has sum 15.</p>
<pre style=3D"background-color: #f8f8f8; border: 1px =
solid #cccccc; font-size: 13px; line-height: 19px; overflow: auto; padding:=
 6px 10px; border-radius: 3px;"><code style=3D"border-radius: 3px; =
font-family: monospace; margin: 0; padding: 0; white-space: pre; =
background: transparent; background-color: transparent; border: none;">  10
 /  \
5    5
 \     \
   2    1
       /
     -1
</code></pre><hr =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
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
----_NmP-bed177143eb38bee-Part_1--
