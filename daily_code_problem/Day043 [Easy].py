Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1ed5:0:0:0:0 with SMTP id m21csp3646326ejj;
        Mon, 6 Apr 2020 08:40:35 -0700 (PDT)
X-Google-Smtp-Source: APiQypLTiT93qOOjteJByoDP3RyAghwxLlue/CBKyDAFRqAi4LOpSsz2ELFVYYvHSz5UORSsQASm
X-Received: by 2002:a05:620a:16c7:: with SMTP id a7mr3194744qkn.337.1586187635036;
        Mon, 06 Apr 2020 08:40:35 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1586187635; cv=none;
        d=google.com; s=arc-20160816;
        b=IawDDjCNMz4Ef3YkufIvQgRK+FTuiMRXSjni0ZP5B1O8B5QCpS2wvuT54Q2G3xx3Sm
         Y7+Pey1/wqdHrkvSAbSv/RmoRXKFXRArgC+C57R0kz2n70zLN0yn9zBzSbijUdmcqHOw
         2HGFSTHT3NbBxdV9UA2buKuJIE0th3guzLfKGJIYT8pBpdMhqX1gU1pchYCj8Sd8hwNv
         6hYjjHvC6XqQHgus7FUOn4j5UVVOYCShYAy4EYs3GJXt0XIsu3Ft03icwPbcMcAQKHOO
         LBfrwozKET5QXVXin6C6/OITXij3oL0GYfthPfhiLW5M8G7Tgh4rAJZfbLQMz6XXygB2
         3WrA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=yaF8tcvNkEX3t0Z2TJz5BnnXENLx6fr6gwZAFWXaIuA=;
        b=lGJKZks19hHqCyLLe49VaYcDtltZ8Afl09W20zvFPSDsUyePgMRb3cJ+mCCMv7yMM0
         1VU0zFwTY6e5b7KpnwGCTScx949j9qsyr9pe8kPt6DeQV2OqfTB5YEWCbjLzAQBzeURv
         o/Qcg9sT3ITVYi824x9Cnvambmigx5AeJ55/aMCbT04k7dDsD5uLqVCLLoOnFEJ0cFnr
         nYfzglCfT2tecRJbW8bMPIo4WoVVXtoUPwg6CvLMP9a7XnSH3237IsG1wWgtN0vfDC+0
         /63O6QAHjYN2aB/QNBsNSI+UXjw3ZhyuxXWv4QuLOA9FrAgu7ay8vX2SUVJX6jgHsV7a
         8qhw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FMWff96+;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=b7lqlrPN;
       spf=pass (google.com: domain of 01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com
Return-Path: <01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id g5si10270396qtu.257.2020.04.06.08.40.34
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-SHA bits=128/128);
        Mon, 06 Apr 2020 08:40:35 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FMWff96+;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=b7lqlrPN;
       spf=pass (google.com: domain of 01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1586187634;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=3T671piyuSPY7ip8bfXvQFjwND5vhbOdRsKC3LhoYmU=;
	b=FMWff96+JuNvA5LCInj/86B+cGVm2eaH4UjRheo0O20t+atzgjuBiyHfzeMvFwkP
	g18EJzYbDvgs/+JjQxmH4A/X9R7cvNeCp6mJRcF4/lIqFKYvXBNheriprIIwNG5FgOF
	rXi6/gBbnUPM4gRXaVJQvP0cyuf0G77ku3ni1LTU=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1586187634;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=3T671piyuSPY7ip8bfXvQFjwND5vhbOdRsKC3LhoYmU=;
	b=b7lqlrPNYm0N8+hp2+6ceNNnsdFeEglYUFV2oDCHCxhlaWBtQkprzltIpD+8jyN1
	8jq3SrdimqRbVYiCN2zzhT0npJ/tFBj4FAhhg3VFr9dCqVsB83pYZf9nXnUdV36m7Ii
	yzeJgYOpxItCvu+lLjLih8S7ZLpW9wqYqegirkNI=
Content-Type: multipart/alternative;
 boundary="--_NmP-0f61eccac84c4e09-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #43 [Easy] 
Message-ID: <01000171502685eb-f2588c0e-09e7-4ded-9238-bf8d689d9ce0-000000@email.amazonses.com>
Date: Mon, 6 Apr 2020 15:40:34 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.04.06-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-0f61eccac84c4e09-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack that has the following=
 methods:

 * push(val), which pushes an element onto the stack
 * pop(), which pops off and returns the topmost element of the stack. If =
there
   are no elements in the stack, then it should throw an error or =
return null.
 * max(), which returns the maximum value in the stack =
currently. If there are
   no elements in the stack, then it should throw =
an error or return null.

Each method should run in constant time.


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
----_NmP-0f61eccac84c4e09-Part_1
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
    <title>Daily Coding Problem: Problem #43 [Easy]
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
Amazon.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Implement a stack that has=
 the following methods:</p>
<ul style=3D"text-align: left; color: #555; =
font-size: 16px; line-height: 1.5em; padding-left: 24px; font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">push(val), which pushes an element onto the =
stack</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">pop(), which pops off and returns the =
topmost element of the stack. If there are no elements in the stack, then =
it should throw an error or return null.</li>
<li style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">max(), which returns the maximum value in the stack currently.=
 If there are no elements in the stack, then it should throw an error or =
return null.</li>
</ul>
<p style=3D"margin-top: 0; color: #555; font-size: =
16px; line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">Each method should =
run in constant time.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box;">
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
----_NmP-0f61eccac84c4e09-Part_1--
