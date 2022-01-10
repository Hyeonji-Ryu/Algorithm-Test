// 문제
// 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

// 출력
// 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10^(-9) 이하이면 정답이다.

use std::io;

fn main() {
    let mut num = String::new();
    io::stdin().read_line(&mut num).expect("wrong numbers");
    let list: Vec<f64> = num.split_whitespace().map(|s| s.parse().expect("parse error")).collect();
    println!("{:}",list[0]/list[1]);
}
