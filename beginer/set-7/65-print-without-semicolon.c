#include <stdio.h>
void main(char str[1000]) {	
	if (scanf("%99[^\n]", &str)) {}
	if (printf("%s", str)) {}
}