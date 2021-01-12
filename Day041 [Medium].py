Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1ed5:0:0:0:0 with SMTP id m21csp1720031ejj;
        Sat, 4 Apr 2020 08:52:48 -0700 (PDT)
X-Google-Smtp-Source: APiQypIk703UUHhwiZc5geyoi5UkIUJKHsxHzl0gfeW/je1kh1WT94PULSYKS8Y3DSb3Ojd7ASYO
X-Received: by 2002:ac8:1207:: with SMTP id x7mr13738556qti.295.1586015568300;
        Sat, 04 Apr 2020 08:52:48 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1586015568; cv=none;
        d=google.com; s=arc-20160816;
        b=Jtb+iX5cmzTk1Cc4F4xP5q6wjHkuUhPale+mb1evU7jfcAI8sYy7COqd0F0MiQgtIb
         KD5XOL4yxxiqglUGYvi4gVA578IOsEOwGnHfz3ocjMaGlO42za3ODU2CyK322r6ZlZVN
         LMoIMH6UKaMNz2xvEIMiqGTf7NCK0YYBoRuC9bDZ9DSuUk+4PcszyV1aqSOUVCFGXMc9
         Xr5WkNd+zaqLyNQaTo2Nov12OJCgon9hXC1Iv3hJvsa3aAjt9J59uGrDx+a4Xe2+P0Za
         ejVbbpfa1L9yzdCtPlT/Sw221CRZpIqkNXxLAHdocQN/SbZhMeq4KxDP4xfyQdAG2F1E
         QC0w==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=grqKDT98eUu40U6ME90SPZpDsTjnJq2iYczd2790fxM=;
        b=oHKO7nMHur/sUaK+yfJi8mWW/8Kt1VNwW6YktVO0Ksj9UzzqCClNKLE7dWlAGMR/Nn
         W0Qf9bt4aGJwAkpqauO+lDdrt4SirtWO5VYkFLZehsdy+kbq536ARs789xLCn0JkTX4d
         J2VTzTJbXsYlnXhip2A4O+pVSfDv7zSTKvAOHrO2ndzi4MYORcW26d/hg5UD2CqDOpsf
         5SG0GletsJaas3H1J1nUkJSh6uipjAuI98fOXkHaUdsHTetYn6d+CsLXrJFRQSwp9JL2
         5upq7DEmZB+Y7g2Vj8Tn2MhBClS0s4kO1VCE+pTmxS8fcMEOB3tPajEpo5cfeKodmELI
         4CvA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=eigrA2Um;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=JsbCKlcI;
       spf=pass (google.com: domain of 0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com
Return-Path: <0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id p50si7650632qtb.219.2020.04.04.08.52.48
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-SHA bits=128/128);
        Sat, 04 Apr 2020 08:52:48 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=eigrA2Um;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=JsbCKlcI;
       spf=pass (google.com: domain of 0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1586015567;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=GmId0YU2uLglySwG4fMWXnQ3TJVjFAM6leNf7VWBDA8=;
	b=eigrA2UmxoN2E4/a3sDFgx7jd/b1VJkZiilTdJ0yRj8K9yWJknuzzxk4HtONm5G3
	rSxKEe3QLRhCsKpwF7zoJvEb41BPB1l/dFEY5tt4/z72/+1PArN1D9e6PxaaNJS6zMz
	1IbFV6rS8vLw5GvrHDug+COe5CCLwDbUEs+VyyEg=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1586015567;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=GmId0YU2uLglySwG4fMWXnQ3TJVjFAM6leNf7VWBDA8=;
	b=JsbCKlcI4pnHJW0/dHxm1B7fFwMGR9ounL5NxtbfXw2GCaQ+To38FhsJo9cpfDco
	a23Ou5JQBCp3JYdrlk/MWqBlxe7RYwfqt5MCWVrFe8oxuTvbij6+Yf6Wm5gJ8dMGO4f
	ALe4MauI6msW8VIXdkjcyFr2IYO92iCI3QuEwVg8=
Content-Type: multipart/alternative;
 boundary="--_NmP-11fecf8fd05c1977-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #41 [Medium] 
Message-ID: <0100017145e4ffca-f975d95a-edfc-4197-90f9-f7b1c31d68c2-000000@email.amazonses.com>
Date: Sat, 4 Apr 2020 15:52:47 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.04.04-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-11fecf8fd05c1977-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an unordered list of flights =
taken by someone, each represented as
(origin, destination) pairs, and a =
starting airport, compute the person's
itinerary. If no such itinerary =
exists, return null. If there are multiple
possible itineraries, return the=
 lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), =
('YUL',
'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should =
return the list
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting =
airport
'COM', you should return null.

Given the list of flights [('A', =
'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
starting airport 'A', you =
should return the list ['A', 'B', 'C', 'A', 'C'] even
though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the =
first
one is lexicographically smaller.


---------------------------------=
-----------------------------------------------

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
----_NmP-11fecf8fd05c1977-Part_1
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
    <title>Daily Coding Problem: Problem #41 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">Given an unordered list of=
 flights taken by someone, each represented as (origin, destination) pairs,=
 and a starting airport,
compute the person&#39;s itinerary. If no such =
itinerary exists, return null. If there are multiple possible itineraries, =
return
the lexicographically smallest one. All flights must be used in the =
itinerary.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">For example, given the =
list of flights [(&#39;SFO&#39;, &#39;HKO&#39;), (&#39;YYZ&#39;, =
&#39;SFO&#39;), (&#39;YUL&#39;, &#39;YYZ&#39;), (&#39;HKO&#39;, =
&#39;ORD&#39;)] and starting airport &#39;YUL&#39;,
you should return the list [&#39;YUL&#39;, &#39;YYZ&#39;, &#39;SFO&#39;, =
&#39;HKO&#39;, &#39;ORD&#39;].</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Given the=
 list of flights [(&#39;SFO&#39;, &#39;COM&#39;), (&#39;COM&#39;, =
&#39;YYZ&#39;)] and starting airport &#39;COM&#39;, you should return null.=
</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: =
1.5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Given the list of flights =
[(&#39;A&#39;, &#39;B&#39;), (&#39;A&#39;, &#39;C&#39;), (&#39;B&#39;, =
&#39;C&#39;), (&#39;C&#39;, &#39;A&#39;)] and starting airport &#39;A&#39;,
you should return the list [&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, =
&#39;A&#39;, &#39;C&#39;] even though [&#39;A&#39;, &#39;C&#39;, =
&#39;A&#39;, &#39;B&#39;, &#39;C&#39;] is also a valid
itinerary. However, the first one is lexicographically smaller.</p>
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
----_NmP-11fecf8fd05c1977-Part_1--
