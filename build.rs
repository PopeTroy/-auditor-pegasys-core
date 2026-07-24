fn main() {
    prost_build::compile_protos(&["proto/audit.proto"], &["proto/"]).unwrap();
}
