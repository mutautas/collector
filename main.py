import phonenumbers, argparse, requests, re
from phonenumbers import timezone, geocoder, carrier
from cfonts import render
from termcolor import colored
from colorama import  Fore, Style
from pyfiglet import Figlet

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='do information gathering on phone numbers')
parser.add_argument('-g', '--github', type=str, help='do information gathering on account github')
parser.add_argument('-i', '--ip', type=str, help='do information gathering on ip')
args = parser.parse_args()

def Banner():
    f = Figlet(font='standard')
    print(colored(f.renderText('collector'), 'green'))
    print(colored("[>] Coded By Galih Ap", 'green'))
    print("\n")

def Main():
    Banner()
    if args.number:
        try: 
            phone_number = phonenumbers.parse(args.number)
            phone_number_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            phone_number_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            ISP = carrier.name_for_number(phone_number, 'en')
            Time_zone = timezone.time_zones_for_number(phone_number) 
            Country = geocoder.country_name_for_number(phone_number, 'en')
            Location = geocoder.description_for_number(phone_number, 'en') 
            print(colored(f"[!] Fetching Phone Number : {args.number}", 'yellow'))
            print(colored(f"[+] {phone_number}", 'green'))
            print(colored(f"[+] International Format : {phone_number_international}", 'green'))           
            print(colored(f"[+] National Format : {phone_number_national}", 'green'))           
            print(colored(f"[+] Time Zone : {Time_zone}", 'green'))
            print(colored(f"[+] ISP : {ISP}", 'green'))
            print(colored(f"[+] Country Found : {Country}", 'green'))
            print(colored(f"[+] Location : {Location}", 'green'))
        except KeyboardInterrupt:
            print(colored("[-] Exit", 'red'))
        except phonenumbers.phonenumberutil.NumberParseException:
            print(colored("[-] WRONG COMMAND!", 'red'))
            print(colored("[!] Example you must enterred : +62xxxxx", 'yellow'))
            
    elif args.github:
            try:
                username = args.github
                url = f'https://api.github.com/users/{username}'
                response = requests.get(url)
                if response.status_code == 200 and requests.codes.ok:
                    data = response.json()
                    print(colored(f"[!] Fetching Github Username : {username}", 'yellow'))
                    print(colored(f"[+] Name : {data['name']}", 'green'))
                    print(colored(f"[+] Id : {data['id']}", 'green'))
                    print(colored(f"[+] Node Id : {data['node_id']}", 'green'))
                    print(colored(f"[+] Gravatar Id : {data['gravatar_id']}", 'green'))
                    print(colored(f"[+] Bio : {data['bio']}", 'green'))
                    print(colored(f"[+] Location : {data['location']}", 'green'))
                    print(colored(f"[+] Email : {data['email']}", 'green'))
                    print(colored(f"[+] Twitter Username : {data['twitter_username']}", 'green'))
                    print(colored(f"[+] Company : {data['company']}", 'green'))
                    print(colored(f"[+] Type : {data['type']}", 'green'))
                    print(colored(f"[+] Blog : {data['blog']}", 'green'))
                    print(colored(f"[+] Followers : {data['followers']}", 'green'))
                    print(colored(f"[+] Following : {data['following']}", 'green'))
                    print(colored(f"[+] Public Gists : {data['public_gists']}", 'green'))
                    print(colored(f"[+] Public Repos : {data['public_repos']}", 'green'))
                    print(colored(f"[+] Created At : {data['created_at']}", 'green'))
                    print(colored(f"[+] Updated At : {data['updated_at']}", 'green'))
                    print(colored(f"[+] Organizations : {data['organizations_url']}", 'green'))
                    print(colored(f"[+] Url : {data['url']}", 'green'))
                    print(colored(f"[+] Html Url : {data['html_url']}", 'green'))
                    print(colored(f"[+] Avatar Url : {data['avatar_url']}", 'green'))
                    print(colored(f"[+] Followers Url : {data['followers_url']}", 'green'))
                    print(colored(f"[+] Following Url : {data['following_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/following", 'green'))
                    print(colored(f"[+] Events Url : {data['events_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/events", 'green'))
                    print(colored(f"[+] Received Events Url : {data['received_events_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/received_events", 'green'))
                    print(colored(f"[+] Gists Url : {data['gists_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/gists", 'green'))
                    print(colored(f"[+] Starred Url : {data['starred_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/starred", 'green'))
                    print(colored(f"[+] Repos Url : {data['repos_url']}", 'green'))
                    print(colored(f"[+] Subscriptions Url : {data['subscriptions_url']}", 'green'))
            except requests.exceptions.ConnectionError:
                print(colored("[-] Error connecting", 'red'))
            except KeyboardInterrupt:
                print(colored("[-] Exit", 'red'))
                
    elif args.ip:
        try:
            if True:           
                ip = args.ip
                url = f'https://ipapi.co/{ip}/json/'
                response = requests.get(url)
                data = response.json()
                match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
                for valid in ip.split('.'):
                    if int(valid) < 0 or int(valid) > 255 or int(valid) == 0000:
                        print(colored('[-] Ip address not valid!', 'red'))
                        print(Fore.GREEN + '-------------INFO-------------')
                        break
                        exit
                print(Fore.YELLOW + f'[!] Fetching On Ip : {ip}')
                for i in data:             
                    print(Fore.GREEN + f'[+] {i} : ',data[i])
        except KeyboardInterrupt:
            print(Fore.RED + '[-] Exit')
        except requests.exceptions.ConnectionError:
            print(colored("[-] Error connecting", 'red'))
        except ValueError:
            print(colored('[-] Ip address not valid!', 'red'))
            
            
if __name__ == "__main__":
    Main()