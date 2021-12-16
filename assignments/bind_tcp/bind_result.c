#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(int argc, char ** argv){
	printf("The numerical representation of the IP address is : %d\n",inet_addr(argv[1]));

	printf("The host byte order of the port number is : %x\n",htons(atoi(argv[2])));

}
