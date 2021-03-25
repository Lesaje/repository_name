#include "header.h"

void dec_in_dig(int num, char* number_arab) {
	int i = 3;
	while (i >= 0) {
		*(number_arab + i) = (num % 10) + '0';
		num /= 10;
		i--;
	}
	return;
}

/*int dec_in_dig_int(int num, int* number_arab_int) {
	int i = 3;
	while (i >= 0) {
		*(number_arab_int + i) = (num % 10) + '0';
		num /= 10;
		i--;
	}
	return;
}*/

void dec_in_rom(char* number_arab, char* number_roman) {
	int i = 0;
	int j = 0;
	int another_counter = 0;
	for (j = 0; j < (*(number_arab + i) - '0'); j++) {
		*(number_roman + j) = 'M';
	}
	j--;

	i++;			

	//go to hundreds

	if (*(number_arab + i) - '0' == 9) {		//'CM' = 900 symbol writing
		j++;
		*(number_roman + j) = 'C';
		j++;
		*(number_roman + j) = 'M';
	}

	if (*(number_arab + i) - '0' == 4) {		//'CD' = 400 symbol writing
		j++;
		*(number_roman + j) = 'C';
		j++;
		*(number_roman + j) = 'D';
	}

	if ((*(number_arab + i) - '0' != 4) && (*(number_arab + i) - '0' != 9)) {	//haha I'm lunatic

		if ((*(number_arab + i) - '0') >= 5) {
			j++;
			*(number_roman + j) = 'D';				//first 500
			for (another_counter=0; another_counter < (*(number_arab + i) - '5'); another_counter++) {		//*(number_arab + i) - '5' equal 7-5 = 2
				j++;
				*(number_roman + j) = 'C';
			}
		}
		else {
			for (another_counter=0; another_counter < (*(number_arab + i) - '0'); another_counter++) {		//just add 1, 2 or 3 'C'
				j++;
				*(number_roman + j) = 'C';
			}
		}
	}

	i++;

	//go to decades

	if (*(number_arab + i) - '0' == 9) {		//'XC' = 90 symbol writing
		j++;
		*(number_roman + j) = 'X';
		j++;
		*(number_roman + j) = 'C';
	}

	if (*(number_arab + i) - '0' == 4) {		//'XL' = 40 symbol writing
		j++;
		*(number_roman + j) = 'X';
		j++;
		*(number_roman + j) = 'L';
	}

	if ((*(number_arab + i) - '0' != 4) && (*(number_arab + i) - '0' != 9)) {	//haha I'm lunatic x2

		if ((*(number_arab + i) - '0') >= 5) {
			j++;
			*(number_roman + j) = 'L';				//first 50
			for (another_counter = 0; another_counter < (*(number_arab + i) - '5'); another_counter++) {		//*(number_arab + i) - '5' equal 7-5 = 2
				j++;
				*(number_roman + j) = 'X';
			}
		}
		else {
			for (another_counter = 0; another_counter < (*(number_arab + i) - '0'); another_counter++) {		//just add 1, 2 or 3 'X'
				j++;
				*(number_roman + j) = 'X';
			}
		}
	}

	i++;

	//go to units

	if (*(number_arab + i) - '0' == 9) {		//'IX' = 9 symbol writing
		j++;
		*(number_roman + j) = 'I';
		j++;
		*(number_roman + j) = 'X';
	}

	if (*(number_arab + i) - '0' == 4) {		//'IV' = 4 symbol writing
		j++;
		*(number_roman + j) = 'I';
		j++;
		*(number_roman + j) = 'V';
	}

	if ((*(number_arab + i) - '0' != 4) && (*(number_arab + i) - '0' != 9)) {	//haha I'm lunatic x3

		if ((*(number_arab + i) - '0') >= 5) {
			j++;
			*(number_roman + j) = 'V';				//first 5
			for (another_counter = 0; another_counter < (*(number_arab + i) - '5'); another_counter++) {		//*(number_arab + i) - '5' equal 7-5 = 2
				j++;
				*(number_roman + j) = 'I';
			}
		}
		else {
			for (another_counter = 0; another_counter < (*(number_arab + i) - '0'); another_counter++) {		//just add 1, 2 or 3 'I'
				j++;
				*(number_roman + j) = 'I';
			}
		}
	}
	
	j++;
	*(number_roman + j) = '\0';

	return;
}
