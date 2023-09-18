class Carro {
  String? carro;
  int? price;

  Carro({this.carro, this.price});
}

void main() {
  Carro p1 = Carro(carro: "Onix", price: 26000);
  print("Esse carro é ${p1.carro} e o seu preço é ${p1.price}");
  // print(p1.carro,p1.price);
}
