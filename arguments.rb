def my_method(a, b, op1:)
  puts a, b, op1
end

my_method(b=2, a=1, op1: 3)

my_options = {
  op1: 3
}
my_method(1, 2, **my_options)