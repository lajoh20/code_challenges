Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:55d0:0:0:0:0 with SMTP id z16csp627931ejp;
        Wed, 9 Sep 2020 08:50:37 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzN5JOgLGSzqCWto6uUSW9ynR+wv2WYHDWORTZmwQnSFPgVH60BwxJe0ifeBzrt4fvmpQKd
X-Received: by 2002:ac8:6d32:: with SMTP id r18mr3967613qtu.246.1599666636859;
        Wed, 09 Sep 2020 08:50:36 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1599666636; cv=none;
        d=google.com; s=arc-20160816;
        b=j6c3QTP0uN9+9/76MDJHCEjtfrWpRk50G6JAzOiLs9E75QsrccigZnejNZWbCUMS6K
         /lF6lFZCrXBNiomcNr4MMHRJCtRDkuCDawA8xZM8fD7LGak9TFCfnXJhMpxTONP4b3W2
         S8YY7AMdmCChFCKTaskG9oy13D3JGgpFRCiQxTClLvAP8QL7wXBsJtAyxV8IGPPhjtmr
         vyxjgGikI7+0HTou432ZBuopjMNliErVSfitDFJenB9shCxkJxIfy44fXdiQaJD1p0Ug
         p2vd+RHah8vQoEOrR0U4HxYB6ZqJJyNXKflJNz5xI8WILckujveaXv2MU/njIWy40s/Q
         tlPA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=JCuh84yyQYb9KYGSutm2hB1588aKodqKpDtl0UtA2Jc=;
        b=LHlTBG1zdqlNXL+pEJhwmnUMQvyEAn7Cme8mxkkoK6w7KXmca8O8gE/PpgEFPQNXoF
         v8D4Jl7k91AoBoRJaTBNAMcubDGSFDyJcVJUMdhS27/jImOgSXXp5Tz5qyCfFYgVk9/K
         QK0qZLsyTHVe9EKeY4nB/SIadqTU0xDHpCNQRC4FxXCVi9ZLaH1jdPTo21lu41x8Ruaf
         VCnK+b3+X9X7NGLw87F3wm/AePLnRI1XnqucgU80mZfcaZGIPHmgKJm8dhoK3+1lzA9w
         VL0uAjBsgBArivJ61JIgm91co9RzME7W0jLN8PMznJS42Wzv9LbHpH0zfjGrNIPUx9HM
         oN7Q==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=UBGL9YF9;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Bwcv5sRA;
       spf=pass (google.com: domain of 01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com
Return-Path: <01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id ec10si1533795qvb.93.2020.09.09.08.50.36
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Wed, 09 Sep 2020 08:50:36 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=UBGL9YF9;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Bwcv5sRA;
       spf=pass (google.com: domain of 01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1599666636;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=MjgZ2K8AKtyCoPIt13FUngZmj34G4dsxC1H4VENh89s=;
	b=UBGL9YF9Vqf4jChcy8lJpO9gn/GKS07UuB3UeyxM3oDSkgMZURulu0rDvwqmJ6jQ
	PgFZ0gS5pmWi2WqbDGMoVsfwfLWZPSz7VlZQPkIZDRiBWPWZubTb04kXDL5Tr897Jbd
	bVJmvANVwIkpe9IHvKlw88ZfKxSK8pCznKw0cgio=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1599666636;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=MjgZ2K8AKtyCoPIt13FUngZmj34G4dsxC1H4VENh89s=;
	b=Bwcv5sRAtNsGjKSgS0OtNRAxIE2cs6b8C+NBgYP0xhGwd10RTng5/qINBuMPCsSo
	vxn+qIjXbloVBAXnnZQcheMH5uM25iE56+c2eFBoTu7uXhV6iwQN3N/QZXOkWesZ6m3
	Px2R3V+0usjaAI0P+/sw2+1lR3NXgAkjJD1laQYw=
Content-Type: multipart/alternative;
 boundary="--_NmP-1cf10d6eb6f3a8ce-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #199 [Hard] 
Message-ID: <01000174738fc4ef-b10e5ace-5fa8-4668-bd42-270a0603c5e9-000000@email.amazonses.com>
Date: Wed, 9 Sep 2020 15:50:36 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.09.09-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-1cf10d6eb6f3a8ce-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of parentheses, find =
the balanced string that can be produced
from it using the minimum number =
of insertions and deletions. If there are
multiple solutions, return any of=
 them.=20

For example, given "(()", you could return "(())". Given "))()("=
, you could
return "()()()()".


------------------------------------------=
--------------------------------------

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
----_NmP-1cf10d6eb6f3a8ce-Part_1
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
    <title>Daily Coding Problem: Problem #199 [Hard]
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
Facebook.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a string of =
parentheses, find the balanced string that can be produced from it using =
the minimum number of insertions and deletions. If there are multiple =
solutions, return any of them. </p>
<p style=3D"margin-top: 0; color: #555;=
 font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, given &quot;(()&quot;, you could return &quot;(())&quot;. Given =
&quot;))()(&quot;, you could return &quot;()()()()&quot;.</p>
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
----_NmP-1cf10d6eb6f3a8ce-Part_1--
