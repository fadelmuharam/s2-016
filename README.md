# s2-016
This is an interactive shell for the s2-016 exploit.
Interactive Shell for CVE-2013-2251

The Apache Struts 2 DefaultActionMapper supports a method for short-circuit navigation state changes by prefixing parameters with "action:" or "redirect:", followed by a desired navigational target expression. This mechanism was intended to help with attaching navigational information to buttons within forms.

Usage: $ python s2-016.py http://site.com

"https://struts.apache.org/docs/s2-016.html"
