public Node buildTree(List<Relation> data){
    HashMap<Integer, Node> map = new HashMap<Integer, Node>();
    Node root = null;

    for(Relation r: data) {
        Node parent, child;

        if ((child = map.get(r.child)) == null) {
            child = new Node();
            child.data = r.child;
            map.put(r.child, child);
        }

        if (r.parent == 0) {
            root = child;
            continue;
        }

        if ((parent = map.get(r.parent)) == null) {
            parent = new Node();
            parent.data = r.parent;
            map.put(r.parent, parent);
        }

        if (r.isLeft) {
            parent.left = child;
        } else {
            parent.right = child;
        }
    }
    return root;
}