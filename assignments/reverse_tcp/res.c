#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc , char ** argv){
	printf("The ip address is : %d\n",inet_addr(argv[1]));
	printf("The port is : %x\n",htons(atoi(argv[2])));
	return 0;
}
