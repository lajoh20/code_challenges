Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:4e0a:0:0:0:0 with SMTP id z10csp1061886eju;
        Fri, 28 Aug 2020 08:58:01 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzDh0S7sF5urIdddAObRd7rJh+f2jwWu1L73woaamVSY2UpT2QR6lRUocEKGRiGZoIKcI+3
X-Received: by 2002:ac8:1805:: with SMTP id q5mr310296qtj.188.1598630281160;
        Fri, 28 Aug 2020 08:58:01 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1598630281; cv=none;
        d=google.com; s=arc-20160816;
        b=hRtjlhEWhkDBtZ2xUPJ05kRLXPYcWzJZFTOvBDDLdZG6VwCvyTfydEtSzXLTI7MrtM
         e35tME+/hZLXzDncmOWbFAdedw3Xi99dA3R8i0CFXOhA35G7Do86E1kfm6jYn7eHQfJE
         W9tgpUPSE/DzzrzfptPQ+jZjUMPRrNm0RP7Ret9Yk9BAyUcVxKS/QhzIpm4imfuLZ7bX
         g0QIkpKKeonvRzVvOWqO2mJHO1IX+D8W5D5fbzkC9cZCERk5y8XFcdH1+JZj6pOafJEg
         Bio7p5kIZAttGp9pv5D2qBARudS8jsAynfWeeClzdlYKaUBiBS1n3fUiQSVFPZCslUx8
         q8aw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=mv+djzT+mtfUpIHkT1TcNC+eCqPZjAze7q5p7kp13lA=;
        b=YO86n4mFF4stCmI1uy+67dmkfqEc1zcSymn+o8AwlV+BfFSHyB/XuFHDkL5+riTXmT
         l6mU/+4AqTDOThzzgVjjxVxus7+HJhhs7C7Zpks/tyadjca6gORxtvq+jM/+2hHdP8LB
         vATemJH1rjp2JzTZOt3+YIU2l/Scf3+njg+tSpgygor84O3TLJePk2GCnIbh9vlTya0T
         +lRjyIE0vBkVF5j2PqZkKb8gpq1BhI1ldhswNrkP3WMr8k9xWpSuA7pQWF4WpHxkrh/J
         VHIvqbQzXsvhh7id1SjZnWpl64rnb5QIj9laN6/b6ZnMe29BLBAv8TN1foleeN789j3q
         ZLAA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=cy4w4fHt;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Qmab6Gge;
       spf=pass (google.com: domain of 0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com
Return-Path: <0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id y15si735090qvx.150.2020.08.28.08.58.00
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 28 Aug 2020 08:58:01 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=cy4w4fHt;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Qmab6Gge;
       spf=pass (google.com: domain of 0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1598630280;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=rrpLz62AuBhGVJH2PpRTGz+57eMD1TsPHvD0kee0C+Q=;
	b=cy4w4fHtBLmRpZjmcO2wYjZ+N9bkXe5sJZ43dq6PpqDKTfJQMYhr45rC2wsFOq7Y
	q/GrTbFoxpZ/9UfFJHAyoFLi7gHuERhr9bbsrCtTN+AR7ezjV18ACR/0C6s4oturPRV
	zwo62HxwxfNRGoL+YiDOQTEh5Cj+tqrsYv4hmfUQ=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1598630280;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=rrpLz62AuBhGVJH2PpRTGz+57eMD1TsPHvD0kee0C+Q=;
	b=Qmab6GgeIfGiw0PyAUJKDgkN9DkQ0KtDnTD9j952W+bhdWfTLsZ0gjrqOmilo3nf
	+BtlOEgdBcHd8flxEPUDLnT5udk6aq+9NSlfdzxmBmcGlnn299RLZyHeLHwt3WWV6f/
	dRnvtF9LnAkCs4u2GksgCe2UfZ8bMcxA2CK30Ne8=
Content-Type: multipart/alternative;
 boundary="--_NmP-764be1d3247875f0-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #187 [Easy] 
Message-ID: <0100017435ca3bb7-fceed585-4821-4ace-b271-8c1108dca5e7-000000@email.amazonses.com>
Date: Fri, 28 Aug 2020 15:58:00 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.08.28-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-764be1d3247875f0-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given given a list of rectangles=
 represented by min and max x- and
y-coordinates. Compute whether or not a =
pair of rectangles overlap each other.
If one rectangle completely covers =
another, it is considered overlapping.

For example, given the following =
rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, =
height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}


return true as the first and third rectangle overlap each other.


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
----_NmP-764be1d3247875f0-Part_1
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
    <title>Daily Coding Problem: Problem #187 [Easy]
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
 Helvetica, sans-serif; box-sizing: border-box;">You are given given a list=
 of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other. If one =
rectangle completely
covers another, it is considered overlapping.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the following =
rectangles:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid =
#cccccc; font-size: 13px; line-height: 19px; overflow: auto; padding: 6px =
10px; border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">{
    &quot;top_left&quot;: (1, 4),
    &quot;dimensions&quot;: (3, 3) # =
width, height
},
{
    &quot;top_left&quot;: (-1, 3),
    &quot;dimensions&quot;: (2, 1)
},
{
    &quot;top_left&quot;: (0, 5),
    &quot;dimensions&quot;: (4, 3)
}
</code></pre><p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">return <code style=3D"font-family: monospace; margin: 0 2px; =
padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">true</code> as the first =
and third rectangle overlap each other.</p>
<hr style=3D"font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;"><a href=3D"https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.com" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Upgrade to premium</a> and get =
in-depth solutions to every problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">If you liked this problem, feel free =
to forward it along so they can <a href=3D"https://www.dailycodingproblem.=
com/" style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">subscribe here</a>! As =
always, shoot us an email if there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Master =
algorithms together on <a href=3D"https://binarysearch.io/?ref=3Ddcp" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Binary Search</a>. Create a room, =
invite your friends, and race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box; font-size: 0.7em;">
  No more? <a href=3D"https://dailycodingproblem.com/unsubscribe?=
unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de6=
58c7d6d6b960ec" style=3D"color: #3869D4; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">Snooze or =
unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
                <table =
class=3D"email-footer" align=3D"center" width=3D"570" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"font-family: Arial, 'Helvetica Neue', Helvetica,=
 sans-serif; box-sizing: border-box; width: 570px; margin: 0 auto; padding:=
 0; -premailer-width: 570px; -premailer-cellpadding: 0; =
-premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box; padding: 35px;">
                      <p class=3D"sub align-center" style=3D"margin-top: 0;=
 line-height: 1.5em; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box; text-align: center; color: #AEAEAE; =
font-size: 12px;">&copy; 2019 Daily Coding Problem. All rights reserved.=
</p>
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
----_NmP-764be1d3247875f0-Part_1--
