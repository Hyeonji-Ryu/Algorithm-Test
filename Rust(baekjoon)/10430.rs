/*
문제
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

출력
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
*/


use std::io;

fn main() {
    //값 받을 변수 생성
    let mut num = String::new();
    //값 가져오기
    io::stdin().read_line(&mut num).expect("wrong numbers");
    //문자열을 숫자 리스트로 변환
    let list: Vec<i32> = num.split_whitespace().map(|s| s.parse().expect("parse error")).collect();
    //프린트
    println!("{}", (list[0]+list[1])%list[2]);
    println!("{}", ((list[0]%list[2])+(list[1]%list[2]))%list[2]);
    println!("{}", (list[0]*list[1])%list[2]);
    println!("{}", ((list[0]%list[2])*(list[1]%list[2]))%list[2]);
}
