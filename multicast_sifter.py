import subprocess
import sys

#List of Multicasts we want to sift through
multicast_streams = [
    #Insert multicast streams here(removed for GitHub push)
]

def play_multicast_streams(streams):
    index = 0
    process = None

    try:
        while True:
            if process:
                process.terminate()  

            print(f"Playing: {streams[index]}")
            process = subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", streams[index], "--volume=256"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            input("Press Enter to switch to the next stream...")  
            #We verify the stream then press enter to move to the next stream essentially adding 1 to index of the Array
            #Doesnt have to be Enter our input request is just waiting for some type of actuation that is not CTRL+C

            index = (index + 1) % len(streams)  #Modulo for when we reach the end of the array we will loop back to the beginning of the array rather than ending the process.
    #Only way to get out of the sifter CTRL + C as we have an enter input to sift through the stream        
    except KeyboardInterrupt:
        print("\nExiting...")
        if process:
            process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    play_multicast_streams(multicast_streams)


