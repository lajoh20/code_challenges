Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:7a4a:0:0:0:0 with SMTP id i10csp868729ejo;
        Sat, 28 Mar 2020 08:41:28 -0700 (PDT)
X-Google-Smtp-Source: ADFU+vv05XaHDCtyiNtU4Bui80J6PkXgZB+DjiNCq8E4TTWX4bx5Tv/s/VwLrXXqUSG9Yxz8ZFNF
X-Received: by 2002:a37:b2c5:: with SMTP id b188mr4203369qkf.98.1585410088037;
        Sat, 28 Mar 2020 08:41:28 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1585410088; cv=none;
        d=google.com; s=arc-20160816;
        b=izbGHAKzHrSwE0zRDX0CBup7zJIlBFokaNEOgU3JNM1Uxc1ydY2lguk/vIggy4lp/b
         Z1xkcKq9Khs05JRnb01zJGBKzL75+8Ldsejx/Bk7G69ApdJpqWcwV3CYDXxH0WOs5tB+
         etZeHrkvkge1FLqbgMgAnq0jIMS/6pFaEdTuf1y2xCP++EWxPC3uF0zx4YH3LkOfIOyH
         j7yP535z+Vjdp0qUetq10Lgb8UNwUdTRfj+Io22vrf8uexG2ozmvbdPa9/yro+bRE3+W
         WHQgM0HvQdquDLIgW8zez3xA/E+aYrTXCT1FoWp/lzlkCdCHMgu86nvut7QKWMCu6kx2
         lYmg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=lHjmZFodgeozy3ei2c98bPdj0FK4MiiyBzmpaxlC1go=;
        b=w9clz74WhLIjDv30AAy9BjmJTQuJJ1MLJdchMf50SeKhZt3GNwTOPM5KOdCwUS+kYA
         rpSRldcV3AoOwotnJ5+XjgrlIPJwcgCoITjtzND52hgrONeWQDTqdY8FZXHfiL73dw+i
         y/voeXe0z2HzG0GbjazGziMy+FzKKJUgzmwZm4UWZ5OyE9IXIs8L0y94tU1xe4OSpuxR
         Qcl/39phPbXaKvbC/eYNqxX+9bYDWD7cU+Nnx4dpzJ94GCEt8pEpazsyV04OFvhHIcQc
         nKzRw83ZKgvmICwmhHBBSUKuOkRg/HBAxNj3wleoae/wLvlecLauC3nfPx2ylLFZURoH
         nLnA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=EYNL8Io1;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=IO6WlL65;
       spf=pass (google.com: domain of 0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com
Return-Path: <0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id c128si5011519qkb.52.2020.03.28.08.41.27
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-SHA bits=128/128);
        Sat, 28 Mar 2020 08:41:28 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=EYNL8Io1;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=IO6WlL65;
       spf=pass (google.com: domain of 0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1585410087;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=2X6Ix7/zytyw3/iWjEnkMrr1IhvKZGZBGfxmuie9big=;
	b=EYNL8Io1h/R0XiAsUHb+DsTPJJTZSe9u0BMHztpqRij/cdBiYq75gaBJMtHgI1aU
	n69HweeZ1V9R+zm2J9vdRZcHFzw75urozzvF34r8CwYlCcIoSkSz5MdRmC9JUhhCuqA
	ZPaCwyz418Cn/dJc7nzGyZ2OLWQwHf57H3Lvyuag=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1585410087;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=2X6Ix7/zytyw3/iWjEnkMrr1IhvKZGZBGfxmuie9big=;
	b=IO6WlL65r8B+Syrda5Yg1HClZ+qRB2k5uuRStp7PsvoN/fzLMYlYvURsvXG1hdN7
	H6RAbiWv/oAiUTJBDP0L9DzDJqno9NGqfPqIvc20f3+sLLengSykumN9cgVx7GVEJaH
	4gODW1vj1QJ7AFJcVUoIHWz/Ty7sHQ7Idfqz5WPY=
Content-Type: multipart/alternative;
 boundary="--_NmP-03fd642a34c9faa8-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #34 [Medium] 
Message-ID: <0100017121ce1895-b476def7-0ee3-4bf9-baeb-b69a53d208d7-000000@email.amazonses.com>
Date: Sat, 28 Mar 2020 15:41:27 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.03.28-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-03fd642a34c9faa8-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that =
can be made by inserting the fewest
number of characters as possible =
anywhere in the word. If there is more than one
palindrome of minimum =
length that can be made, return the lexicographically
earliest one (the first one alphabetically).

For example, given the string=
 "race", you should return "ecarace", since we can
add three letters to it =
(which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding =
three
letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle"=
.


-----------------------------------------------------------------------=
---------

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe=
?email=3Dlewisjohnson1066334%40gmail.com]=20
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
----_NmP-03fd642a34c9faa8-Part_1
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
    <title>Daily Coding Problem: Problem #34 [Medium]
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
Quora.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a string, find the =
palindrome that can be made by inserting the fewest number of characters as=
 possible anywhere in the word.
If there is more than one palindrome of =
minimum length that can be made, return the lexicographically earliest one =
(the first one alphabetically).</p>
<p style=3D"margin-top: 0; color: #555;=
 font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, given the string &quot;race&quot;, you should return =
&quot;ecarace&quot;, since we can add three letters to it (which is the =
smallest amount to make a palindrome).
There are seven other palindromes =
that can be made from &quot;race&quot; by adding three letters, but =
&quot;ecarace&quot; comes first alphabetically.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">As another example, given the string =
&quot;google&quot;, you should return &quot;elgoogle&quot;.</p>
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
----_NmP-03fd642a34c9faa8-Part_1--
